#!/usr/bin/env bash
# [bash_init]-[BEGIN]
# Exit whenever it encounters an error, also known as a non–zero exit code.
set -o errexit
# Return value of a pipeline is the value of the last (rightmost) command to exit with a non-zero status,
#   or zero if all commands in the pipeline exit successfully.
set -o pipefail
# Treat unset variables and parameters other than the special parameters ‘@’ or ‘*’ as an error when performing parameter expansion.
set -o nounset
## Print a trace of commands.
#set -o xtrace
# [bash_init]-[END]

# Download current repo as a zip file and extract it
# First argument: name of the archive file to create (without extension)

amount_of_tasks="${1:-10}"



# function to create a single task folder by parent_path and task_number
create_task_folder() {
    local parent_path="${1}"
    local task_number="${2}"

    local task_folder_name="task_${task_number}"
    local task_folder_path="${parent_path}/${task_folder_name}"

    # Check if the task folder already exists
    if [[ -d "${task_folder_path}" ]]; then
        echo "Task folder ${task_folder_path} already exists. Skipping creation."
        return
    fi

    mkdir --parents "${task_folder_path}"

    # Create empty __init__.py file inside the task folder
    touch "${task_folder_path}/__init__.py"
    # Create main.py file with default content
    cat <<EOF > "${task_folder_path}/main.py"
def main() -> None:
    print("This is task ${task_number}.")


if __name__ == "__main__":
    main()
EOF

    # Create task.md file with a template content
    cat <<EOF > "${task_folder_path}/task.md"
# Task ${task_number}

Describe the task here.

## Acceptance criteria

Describe the acceptance criteria here.
EOF

  # Create tests folder with __init__.py and test_main.py
    local tests_folder_path="${task_folder_path}/tests"
    mkdir --parents "${tests_folder_path}"
    touch "${tests_folder_path}/__init__.py"
    cat <<EOF > "${tests_folder_path}/test_main.py"
import pytest

from ${package_name_normalized}.task_${task_number}.main import main


@pytest.mark.parametrize(
    ("input_data", "expected_output"),
    [
        # Add test cases here
        (None, None),
    ],
)
@pytest.mark.skip(reason="No tests implemented yet.")
def test_main(
    input_data: None,  # noqa: ARG001
    expected_output: None,  # noqa: ARG001
) -> None:
    # Implement test logic here
    # result = main()
    # assert result == expected_output
    main()
EOF

}

path_to_project_root=$(git rev-parse --show-toplevel)

# Go to src/<PackageName>

path_to_src_dir="${path_to_project_root}/src"

# Get from toml file the package name
package_name_raw=$(grep --perl-regexp --only-matching '(?<=^name = ")[^"]*' "${path_to_project_root}/pyproject.toml" | head -n 1)

# Normalize package name to python module name rules
package_name_normalized=$(echo "${package_name_raw}" | tr '-' '_' )

path_to_package_dir="${path_to_src_dir}/${package_name_normalized}"

# Create task folders
for (( i=1; i<=amount_of_tasks; i++ )); do
    create_task_folder "${path_to_package_dir}" "${i}"
done

# Git add the created folders
git add "${path_to_package_dir}/task_"*

# Final message
echo "Created ${amount_of_tasks} task folders inside: ${path_to_package_dir}"
