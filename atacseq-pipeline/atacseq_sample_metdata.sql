CREATE TABLE atacseq_sample_table (
	genome_assembly VARCHAR(20) NOT NULL DEFAULT 'hg38',
	pipeline_version VARCHAR(20) NOT NULL,
	run_date DATE NOT NULL,
	sequencing_type VARCHAR(20) DEFAULT 'pair-ended',
	qc_status VARCHAR(20) NOT NULL CHECK (qc_status IN ('pass', 'fail')),
	qc_tss_enrichment_score FLOAT NOT NULL CHECK (qc_tss_enrichment >= 0),
	qc_frip_score FLOAT NOT NULL CHECK (qc_frip_score BETWEEN 0 AND 1),
	qc_library_complexity FLOAT NOT NULL CHECK (qc_library_complexity >= 0),
	qc_mito_reads_percent FLOAT NOT NULL CHECK (qc_mito_reads_percent BETWEEN 0 AND 100),
	qc_total_peaks_called INT NOT NULL CHECK (qc_total_peaks_called >= 0),
	qc_duplicate_rate FLOAT NOT NULL CHECK (qc_duplicate_rate BETWEEN 0 AND 1),
	qc_mapped_reads BIGINT NOT NULL CHECK (qc_mapped_reads >= 0),
	qc_fragment_size_median FLOAT NOT NULL CHECK (qc_fragment_size_median > 0),
        FOREIGN KEY (sample_id) REFERENCES sample_sheet_metadata(sample_id)
);
	
	  
