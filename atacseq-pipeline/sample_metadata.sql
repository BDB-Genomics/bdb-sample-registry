CREATE TABLE sample_sheet_metadata (
	sample_id TEXT PRIMARY KEY, 
	replicate INT  NOT NULL CHECK (replicate > 0 ),
	condition TEXT NOT NULL, 
	fastq_r1 TEXT NOT NULL, 
	fastq_r2 TEXT NOT NULL, 
        control_sample_id TEXT NULL
	FOREIGN KEY (control_sample_id) REFERENCES sample_sheet_metadata(sample_id)
);
