# Dump drankbeheer database compress with gzip and backup via rclone to Google Drive
# file: dump-{data}.sql.gz

pg_dump drankbeheer > dump.sql
gzip dump.sql
# change file name to dump-{date}.sql.gz
# data in format: DD-MM-YYYY
mv dump.sql.gz dump-$(date +%d-%m-%Y).sql.gz
rclone sync dump-$(date +%d-%m-%Y).sql.gz gdrive:backups/
