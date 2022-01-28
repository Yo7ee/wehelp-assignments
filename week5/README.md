# Week5作業

## Section
### [要求三](#question3)
### [要求四](#question4)
### [要求五](#question5)

### question3
要求三：SQL CRUD
### 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。

```mysql
INSERT INTO member (name, username, password) VALUES ("test1", "test", "test");
INSERT INTO member (name, username, password) VALUES ("LUCY",
 "lucy", "lucy"), ("Bob", "bob", "bob");
```

### 使用 SELECT 指令取得所有在 member 資料表中的會員資料。
```mysqql
SELECT * FROM member;
```
[image](https://github.com/Yo7ee/wehelp-assignments/blob/65159405d212fb83ce68f12aaf6dcb16cbf2664e/week5/screenshot/%E6%88%AA%E5%9C%96%202022-01-25%20%E4%B8%8B%E5%8D%883.33.33.png)
### 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
```mysql
SELECT * FROM member ORDER by time DESC;
```
[image](https://github.com/Yo7ee/wehelp-assignments/blob/65159405d212fb83ce68f12aaf6dcb16cbf2664e/week5/screenshot/%E6%88%AA%E5%9C%96%202022-01-25%20%E4%B8%8B%E5%8D%883.53.02.png)

### 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
```mysql
SELECT * FROM member ORDER BY time DESC LIMIT 1,3;
```
[image](https://github.com/Yo7ee/wehelp-assignments/blob/65159405d212fb83ce68f12aaf6dcb16cbf2664e/week5/screenshot/%E6%88%AA%E5%9C%96%202022-01-25%20%E4%B8%8B%E5%8D%884.24.37.png)

### 使用 SELECT 指令取得欄位 username 是 test 的會員資料。
```mysql
SELECT * FROM member where username="test";
```
[image](https://github.com/Yo7ee/wehelp-assignments/blob/65159405d212fb83ce68f12aaf6dcb16cbf2664e/week5/screenshot/%E6%88%AA%E5%9C%96%202022-01-25%20%E4%B8%8B%E5%8D%889.51.39.png)

### 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
```mysql
SELECT * FROM member where username="test" and password="test";
```
[image](https://github.com/Yo7ee/wehelp-assignments/blob/65159405d212fb83ce68f12aaf6dcb16cbf2664e/week5/screenshot/%E6%88%AA%E5%9C%96%202022-01-25%20%E4%B8%8B%E5%8D%889.58.24.png)

### 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位
改成 test2。
```mysql
UPDATE member SET username="test2" WHERE username="test";
SELECT * FROM member;
```
[image](https://github.com/Yo7ee/wehelp-assignments/blob/65159405d212fb83ce68f12aaf6dcb16cbf2664e/week5/screenshot/%E6%88%AA%E5%9C%96%202022-01-25%20%E4%B8%8B%E5%8D%8810.05.16.png)

### question4
要求四：SQL Aggregate Functions

### 更新table的follower_count number
```mysql
UPDATE member SET follower_count = CASE id WHEN 1 THEN 4 WHEN 3 THEN 10 WHEN 4 THEN 500 WHEN 5 THEN 22 END WHERE id in(1,3,4,5);
```
[image](https://github.com/Yo7ee/wehelp-assignments/blob/65159405d212fb83ce68f12aaf6dcb16cbf2664e/week5/screenshot/%E6%88%AA%E5%9C%96%202022-01-25%20%E4%B8%8B%E5%8D%8810.39.51.png)

### 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
```mysql
SELECT COUNT(id) FROM member;
```
[image](https://github.com/Yo7ee/wehelp-assignments/blob/65159405d212fb83ce68f12aaf6dcb16cbf2664e/week5/screenshot/%E6%88%AA%E5%9C%96%202022-01-25%20%E4%B8%8B%E5%8D%8810.16.36.png)

### 取得 member 資料表中，所有會員 follower_count 欄位的總和。
```mysql
SELECT SUM(follower_count) FROM member;
```
[image](https://github.com/Yo7ee/wehelp-assignments/blob/65159405d212fb83ce68f12aaf6dcb16cbf2664e/week5/screenshot/%E6%88%AA%E5%9C%96%202022-01-25%20%E4%B8%8B%E5%8D%8810.32.20.png)

### 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
```mysql
SELECT AVG(follower_count) FROM member;
```
[image](https://github.com/Yo7ee/wehelp-assignments/blob/65159405d212fb83ce68f12aaf6dcb16cbf2664e/week5/screenshot/%E6%88%AA%E5%9C%96%202022-01-25%20%E4%B8%8B%E5%8D%8810.31.45.png)


## question5
要求五:SQL JOIN (Optional)

### message資料庫
```mysql
CREATE TABLE message(
    -> id bigint PRIMARY KEY AUTO_INCREMENT COMMENT'獨立編號',
    -> member_id bigint NOT NULL COMMENT'留言者會員編號',
    -> content varchar(255) NOT NULL COMMENT'留言內容',
    -> time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT'
```
[image](https://github.com/Yo7ee/wehelp-assignments/blob/65159405d212fb83ce68f12aaf6dcb16cbf2664e/week5/screenshot/%E6%88%AA%E5%9C%96%202022-01-26%20%E4%B8%8A%E5%8D%8810.40.42.png)

### 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。
```mysql
SELECT member.name, message.content FROM member INNER JOIN message ON member.id = message.member_id;
```
[image](https://github.com/Yo7ee/wehelp-assignments/blob/65159405d212fb83ce68f12aaf6dcb16cbf2664e/week5/screenshot/%E6%88%AA%E5%9C%96%202022-01-26%20%E4%B8%8A%E5%8D%8811.58.02.png)

### 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。
```mysql
SELECT member.name, message.content FROM member INNER JOIN message ON member.id = message.member_id WHERE member.username="test2";
```
[image](https://github.com/Yo7ee/wehelp-assignments/blob/65159405d212fb83ce68f12aaf6dcb16cbf2664e/week5/screenshot/%E6%88%AA%E5%9C%96%202022-01-26%20%E4%B8%8B%E5%8D%8812.00.48.png)