-- 데이터베이스 생성
CREATE DATABASE test;

-- 데이터베이스 사용
USE test;

-- user 테이블 생성
CREATE TABLE user (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL
);

-- 예제 데이터 삽입
INSERT INTO user (name, age) VALUES ('John', 28);
INSERT INTO user (name, age) VALUES ('Jane', 32);
INSERT INTO user (name, age) VALUES ('Alice', 24);
INSERT INTO user (name, age) VALUES ('Bob', 27);
INSERT INTO user (name, age) VALUES ('Charlie', 29);
