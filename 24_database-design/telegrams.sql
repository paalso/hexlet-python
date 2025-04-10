-- В этом задании вам необходимо спроектировать схему базы данных для небольшого
-- мессенджера "Телеграммы".

-- Пользователи регистрируются в мессенджере с помощью мобильного номера телефона.
-- Они указывают свой никнейм и по желанию могут указать имя и фамилию.

-- Любой пользователь может создать канал указать его название и slug,
-- который будет частью ссылки на этот канал.

-- В каналах нет системы ролей, есть только админы и обычные пользователи.

-- Любой пользователь может писать в любой канал.

DROP TABLE IF EXISTS channel_messages;
DROP TABLE IF EXISTS channel_members;
DROP TABLE IF EXISTS channels;
DROP TABLE IF EXISTS users;

CREATE TABLE users(
  id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  username VARCHAR(32) UNIQUE NOT NULL,
  phone_number VARCHAR(16) UNIQUE NOT NULL,
  first_name VARCHAR(50),
  last_name VARCHAR(50)
);

CREATE TABLE channels (
  id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  title VARCHAR(255) NOT NULL,
  slug VARCHAR(255) UNIQUE NOT NULL,
  creator_id BIGINT REFERENCES users(id) NOT NULL
);

CREATE TABLE channel_members(
  user_id BIGINT REFERENCES users(id) NOT NULL,
  channel_id BIGINT REFERENCES channels(id) NOT NULL,
  is_admin BOOLEAN NOT NULL,
  UNIQUE(user_id, channel_id)
);

CREATE TABLE channel_messages(
  id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  content TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  user_id BIGINT REFERENCES users(id) NOT NULL,
  channel_id BIGINT REFERENCES channels(id) NOT NULL
);

-- Data Insertion

INSERT INTO users (username, phone_number, first_name, last_name)
VALUES 
  ('john_doe', '+7123456789', 'John', 'Doe'),
  ('mary_sue', '+7120696969', 'Mary', 'Sue');

INSERT INTO channels (title, slug, creator_id)
VALUES
  ('General', 'general', 1),
  ('Pretty Girls', 'prettygirls', 2);

INSERT INTO channel_members (user_id, channel_id, is_admin)
VALUES
  (1, 1, true),
  (2, 1, false),
  (2, 2, true);

INSERT INTO channel_messages (content, created_at, user_id, channel_id)
VALUES
  ('Hello everyone!', NOW(), 1, 1),
  ('Hello guys! Welcome', NOW(), 2, 2),
  ('Hello pretty girls!', NOW(), 1, 2);
