CREATE TABLE IF NOT EXISTS welldiary (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    long_well_name TEXT NOT NULL DEFAULT '',
    field_name TEXT NOT NULL DEFAULT 'Приразломное',
    drilled TEXT NOT NULL DEFAULT 'Не пробурена'
    )
