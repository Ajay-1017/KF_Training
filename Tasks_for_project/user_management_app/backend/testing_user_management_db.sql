-- 1) Tell me the name of the database this connection is currently using. 
-- SELECT current_database(); 


-- 2) PostgreSQL is basically answering : These are the tables I found in the public schema.
-- SELECT table_name
-- FROM information_schema.tables
-- WHERE table_schema = 'public';


-- 3) I`nspect the columns inside those tables
-- SELECT
--     table_name,
--     column_name,
--     data_type
-- FROM information_schema.columns
-- WHERE table_schema = 'public'
-- ORDER BY table_name, ordinal_position;



-- 4) Learn PostgreSQL constraints
-- SELECT
--     tc.table_name,
--     tc.constraint_name,
--     tc.constraint_type
-- FROM information_schema.table_constraints AS tc
-- WHERE tc.table_schema = 'public'
-- ORDER BY tc.table_name, tc.constraint_type;


-- 5) ON DELETE CASCADE
-- SELECT
--     tc.table_name,
--     tc.constraint_name,
--     ccu.table_name AS referenced_table,
--     ccu.column_name AS referenced_column
-- FROM information_schema.table_constraints AS tc
-- JOIN information_schema.constraint_column_usage AS ccu
--     ON tc.constraint_name = ccu.constraint_name
-- WHERE tc.constraint_type = 'FOREIGN KEY'
--   AND tc.table_schema = 'public';

SELECT * from sessions;


