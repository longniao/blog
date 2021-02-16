-- admin definition

CREATE TABLE admin (
	create_at DATETIME, 
	update_at DATETIME, 
	id INTEGER NOT NULL, 
	username VARCHAR(20), 
	password_hash VARCHAR(128), 
	blog_title VARCHAR(60), 
	blog_sub_title VARCHAR(100), 
	name VARCHAR(30), 
	about TEXT, 
	PRIMARY KEY (id)
);

CREATE INDEX ix_admin_id ON admin (id);



-- category definition

CREATE TABLE category (
	create_at DATETIME, 
	update_at DATETIME, 
	id INTEGER NOT NULL, 
	name VARCHAR(30), 
	PRIMARY KEY (id), 
	UNIQUE (name)
);

CREATE INDEX ix_category_id ON category (id);


-- link definition

CREATE TABLE link (
	create_at DATETIME,
	update_at DATETIME,
	id INTEGER NOT NULL,
	name VARCHAR(30),
	url VARCHAR(255),
	PRIMARY KEY (id)
);


-- post definition

CREATE TABLE post (
	create_at DATETIME, 
	update_at DATETIME, 
	id INTEGER NOT NULL, 
	title VARCHAR(100), 
	body TEXT, 
	status INTEGER, 
	reading INTEGER, 
	category_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(category_id) REFERENCES category (id)
);

CREATE INDEX ix_post_id ON post (id);


-- comment definition

CREATE TABLE comment (
	create_at DATETIME, 
	update_at DATETIME, 
	id INTEGER NOT NULL, 
	author VARCHAR(30), 
	content TEXT, 
	post_id INTEGER, 
	replied_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(post_id) REFERENCES post (id), 
	FOREIGN KEY(replied_id) REFERENCES comment (id)
);

CREATE INDEX ix_comment_id ON comment (id);