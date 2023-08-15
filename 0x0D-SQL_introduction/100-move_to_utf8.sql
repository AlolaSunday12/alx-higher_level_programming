-- Script to convert hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)

-- Convert the database to utf8mb4 character set and utf8mb4_unicode_ci collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the table first_table to utf8mb4 character set and utf8mb4_unicode_ci collation
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the name field in first_table to utf8mb4 character set and utf8mb4_unicode_ci collation
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
