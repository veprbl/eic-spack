generate_new_version_data()
{
  cat <<EOF
{
  "title": "New package versions found",
  "body": "$(cat gh-new-version.log | sed -z 's/\n/\\n/g')\n"
}
EOF
}
cat gh-new-version.log
echo $(generate_new_version_data)
if [[ -f gh-new-version.log ]]; then
  curl -s -H "Authorization: Bearer ${COMMENT_BOT_TOKEN}" \
   -X POST -d "$(generate_new_version_data)"  \
   "https://api.github.com/repos/${GITHUB_REPOSITORY}/issues"
else
  echo "No new versions found"
fi
