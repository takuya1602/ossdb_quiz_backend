create table grades (
    id serial primary key,
    name varchar(10),
    slug varchar(10),
);

create table categories (
    id serial primary key,
    name varchar(20),
    slug varchar(20),
);

create table sub_categories (
    id serial primary key,
    name varchar(50),
    parent_category_id integer references categories(id)
);

create table questions (
    id serial primary key,
    number int,
    title text,
    commentary text,
    grade_id integer references grades(id),
    sub_category_id integer references sub_categories(id)
);

create table choices (
    id serial primary key,
    content text,
    is_answer boolean,
    parent_problem_id integer references problems(id)
);

insert into
    grades (name)
values
    ('name'),
    ('silver');

insert into
    categories ('name', 'slug', 'parent_category_id')
values
    ('運用管理', 'management'),
    ('一般知識', 'knowledge'),
    ('開発/SQL', 'development'),
    ('性能監視', 'monitoring'),
    ('パフォーマンスチューニング', 'performance'),
    ('障害対応', 'trouble');