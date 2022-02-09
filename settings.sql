-- settings.sql
CREATE DATABASE gallery;
CREATE USER galleryuser WITH PASSWORD 'gallery';
GRANT ALL PRIVILEGES ON DATABASE gallery TO galleryuser;