DROP TABLE IF EXISTS taches;

CREATE TABLE taches (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  titre TEXT NOT NULL,
  description TEXT,
  date_echeance TEXT,
  est_terminee INTEGER NOT NULL DEFAULT 0
);
