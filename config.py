from dataclasses import dataclass
from environs import Env


@dataclass
class Hidden:
    mailbox: str
    mail_pass: str
    mail_path: str
    subject_keywords_xls: str
    subject_keywords_apple: str
    yadisk: str
    postgresql_login: str
    postgresql_password: str
    postgresql_host: str
    postgresql_port: int
    postgres_db_name: str


def load_config(path: str = None):
    env = Env()
    env.read_env()
    return Hidden(
        mailbox=env.str("MAIL_BOX"),
        mail_pass=env.str("MAIL_PASS"),
        mail_path=env.str("MAIL_PATH"),
        subject_keywords_xls=env.str("SUBJECT_KEYWORDS_XLS"),
        subject_keywords_apple=env.str("SUBJECT_KEYWORDS_APPLE"),
        yadisk=env.str("YATOKEN"),
        postgresql_login=env.str("POSTGRESQL_LOGIN"),
        postgresql_password=env.str("POSTGRESQL_PASSWORD"),
        postgresql_host=env.str("POSTGRESQL_HOST"),
        postgresql_port=env.int("POSTGRESQL_PORT"),
        postgres_db_name=env.str("POSTGRESQL_DB_NAME"),

    )


hidden_vars = load_config('..env')
