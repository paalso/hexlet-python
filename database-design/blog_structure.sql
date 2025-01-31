-- В этом задании вам предстоит создать структуру таблиц для блога.
-- Блог содержит следующие сущности - пользователи, посты, комментарии, лайки.

-- Пользователи могут писать посты, ставить лайк к постам и оставлять комментарии к постам.
-- У поста есть заголовок и тело поста неограниченной длины.
-- У комментария есть только содержимое, которое может быть не ограничено.
-- Все поля обязательные и не могут быть пустыми.

-- У пользователя есть только электронная почта, которая уникальна.

DROP TABLE IF EXISTS likes;
DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE posts (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    user_id BIGINT REFERENCES users(id) NOT NULL,
    title VARCHAR(255) NOT NULL,
    body TEXT NOT NULL
);

CREATE TABLE post_comments (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    post_id BIGINT REFERENCES posts(id) NOT NULL,
    user_id BIGINT REFERENCES users(id) NOT NULL,
    body TEXT NOT NULL
);

CREATE TABLE post_likes (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    post_id BIGINT REFERENCES posts(id) NOT NULL,
    user_id BIGINT REFERENCES users(id) NOT NULL,
    UNIQUE (post_id, user_id) -- предотвращает повторные лайки
);

-- Вставка пользователей
INSERT INTO users (email)
VALUES
    ('matthew79@example.com'),
    ('qoliver@example.org'),
    ('georgerodriguez@example.com'),
    ('sherriburnett@example.com'),
    ('gcoleman@example.net');

-- Вставка постов
INSERT INTO posts (user_id, title, body)
VALUES
    (1, 'Just five all never', 'Church to central else set. Support coach perhaps reduce war billion. Want teach be thought Mrs. Hit citizen indeed million detail staff option. Successful authority about. Which mean teach front.'),
    (1, 'Plan none pattern cover', 'Toward prevent physical technology would than. Officer until may nothing sound bill staff. Leg card well indicate because dinner old. Anything card president dinner clear both together. Director each carry kind boy.'),
    (2, 'Travel executive place in order', 'Parent third few. Born simple meet career force resource. Soon suddenly manager share full year join. Response especially heavy might.'),
    (3, 'Network more economy and', 'Great social sea opportunity while both shake. During condition several analysis pay story hold describe. Official across picture service.'),
    (5, 'Let model', 'Religious event official plan move at. Film because business best. Perform movie represent control above car. Indeed of affect month sit section accept. The partner state customer second unit particular. Rule ready language both.');

INSERT INTO post_comments (post_id, user_id, body)
VALUES
    (1, 2, 'Great post!'),
    (1, 3, 'Thanks for the information.'),
    (2, 1, 'Interesting perspective.'),
    (2, 4, 'This reminded me of a book.'),
    (3, 5, 'Totally agree!'),
    (4, 2, 'You have a talent for writing!'),
    (5, 3, 'Looking forward to more.');

INSERT INTO post_likes (post_id, user_id)
VALUES
    (1, 2),
    (1, 3),
    (2, 1),
    (2, 4),
    (3, 5),
    (3, 1),
    (4, 2),
    (5, 3);
