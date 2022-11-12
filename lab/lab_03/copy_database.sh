original_path=/home/gero/.var/app/org.mozilla.Thunderbird/.thunderbird/eal9c2od.default-default/global-messages-db.sqlite
temporary_path=./messages_copy.db
remote_path=/home/osi/team6/lab_03/messages_copy.db

cp $original_path $temporary_path

scp $temporary_path team6@team-osi:$remote_path
