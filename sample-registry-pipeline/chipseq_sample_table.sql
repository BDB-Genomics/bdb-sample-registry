CREATE TABLE chipseq_sample_table (
	sample_id TEXT PRIMARY KEY,
	genome_assembly VARCHAR(20) DEFAULT 'hg38',
	spikein_genome VARCHAR(20)  DEFAULT 'ecoli',
	pipeline_version VARCHAR(20) NOT NULL ,
	run_date DATE NOT NULL,
	qc_status VARCHAR(10) CHECK (qc_status IN ('pass', 'fail')),
	qc_mapped_reads BIGINT CHECK (qc_mapped_reads >= 0),
	qc_mito_reads_percent FLOAT CHECK (qc_mito_reads_percent BETWEEN 0 AND 100),
	qc_duplicate_rate FLOAT CHECK (qc_duplicate_rate BETWEEN 0 AND 1), 
	qc_fragment_size_median FLOAT CHECK (qc_fragment_size_median > 0),
	qc_library_complexity FLOAT CHECK (qc_library_complexity BETWEEN 0 AND 1), 
	qc_spikein_scaling_called FLOAT CHECK (qc_spikein_scaling_called > 0), 
	qc_total_peaks_called BIGINT CHECK (qc_total_peaks_called >= 0),
        FOREIGN KEY (sample_id) REFERENCES sample_sheet_metadata(sample_id)
);
