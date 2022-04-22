CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);

CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO Categories ('label') VALUES ('Updates');
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Tags ('label') VALUES ('Python');
INSERT INTO Tags ('label') VALUES ('React');
INSERT INTO Tags ('label') VALUES ('Al Green');
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');
INSERT INTO Posts VALUES (null, 1, 1, 'Noob 2', "2022-04-20", "", "I am still new, but a software developer nonetheless.", 1);
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (1, 1);
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (1, 2);
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (2, 2);
INSERT INTO PostTags ('post_id', 'tag_id') VALUES (2, 3);
INSERT INTO Subscriptions ('follower_id', 'author_id', 'created_on') VALUES (1, 2, "2022-04-20");
INSERT INTO Subscriptions ('follower_id', 'author_id', 'created_on') VALUES (2, 3, "2022-04-20");
INSERT INTO Subscriptions ('follower_id', 'author_id', 'created_on') VALUES (3, 4, "2022-04-20");
INSERT INTO Subscriptions ('follower_id', 'author_id', 'created_on') VALUES (4, 1, "2022-04-20");

INSERT INTO Comments ('post_id', 'author_id', 'content') VALUES (1, 2, "This is a comment");

SELECT
  id,
  user_id,
  category_id,
  title,
  publication_date,
  image_url,
  content,
  approved
FROM Posts;

-- DROP TABLE Posts

SELECT
  p.id,
  p.user_id,
  p.category_id,
  p.title,
  p.publication_date,
  p.image_url,
  p.content,
  p.approved,
  c.label category_label,
  u.first_name,
  t.label
FROM PostTags pt
JOIN Posts p
  ON p.id = pt.post_id
JOIN Tags t
  ON t.id = pt.tag_id
JOIN Categories c
  ON c.id = p.category_id
JOIN Users u
  ON u.id = p.user_id
WHERE t.label LIKE "%py%";


SELECT
    posts.title
FROM Posts p
JOIN Categories c
  ON c.id = p.category_id
JOIN Users u
  ON u.id = p.user_id;


-- test for get_all_users
SELECT
  u.username,
  u.first_name,
  u.last_name,
  u.email
FROM users u
ORDER BY u.username ASC

SELECT
    u.id,
    u.username,
    u.first_name,
    u.last_name,
    u.email,
    u.bio,
    u.profile_image_url,
    u.created_on,
    u.active
FROM users u
WHERE u.id = ?