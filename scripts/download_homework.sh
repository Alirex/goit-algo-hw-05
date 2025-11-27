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

archive_file_part="${1}"


# Check if have ".zip" extension the provided archive file name.
# If not, add it. Else, keep it as is.
# Use `archive_file_name` variable to store the final archive file name.
if [[ "${archive_file_part}" == *.zip ]]; then
    archive_file_name="${archive_file_part}"
else
    archive_file_name="${archive_file_part}.zip"
fi

repo_url=$(git config --get remote.origin.url)

# Remove possible ".git" suffix from the repo URL
repo_url="${repo_url%.git}"

path_to_project_root=$(git rev-parse --show-toplevel)
path_to_files_dir="${path_to_project_root}/files"

path_to_archive_file="${path_to_files_dir}/${archive_file_name}"

# Download the repo as a zip file
curl --silent --show-error --location --output "${path_to_archive_file}" "${repo_url}/archive/refs/heads/main.zip"

# Final message
echo "Archive file created at: ${path_to_archive_file}"


folder_with_archive=$(dirname "${path_to_archive_file}")

echo "--- Summary ---"

echo "Archive stored in folder: file://${folder_with_archive}"

echo "URL to repo:"
echo "${repo_url}"
