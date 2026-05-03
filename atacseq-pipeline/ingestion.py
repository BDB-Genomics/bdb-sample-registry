import psycopg2


def _validate_inputs(conn, sample, required_keys=None):
    if not all(hasattr(conn, name) for name in ("cursor", "commit", "rollback")):
        raise TypeError("conn must provide cursor(), commit(), and rollback().")

    if not isinstance(sample, dict):
        raise TypeError(f"The sample must be a python dict, got {type(sample).__name__}.")

    if required_keys:
        for sample_id, record in sample.items():
            if not isinstance(record, dict):
                raise TypeError(f"Record for sample '{sample_id}' must be a dict, got {type(record).__name__}.")
            missing = [key for key in required_keys if key not in record]
            if missing:
                raise KeyError(f"Sample '{sample_id}' is missing required keys: {', '.join(missing)}")


def atacseq_sample_metadata(conn, sample):
    """Populate the output features table for ATAC-seq pipeline results."""
    required_keys = [
        "genome_assembly", "pipeline_version", "run_date", "sequencing_type",
        "qc_status", "qc_tss_enrichment_score", "qc_frip_score",
        "qc_library_complexity", "qc_mito_reads_percent", "qc_total_peaks_called",
        "qc_duplicate_rate", "qc_mapped_reads", "qc_fragment_size_median"
    ]
    _validate_inputs(conn, sample, required_keys=required_keys)

    try:
        with conn.cursor() as cursor:
            for sample_id, record in sample.items():
                row = (
                    sample_id,
                    record["genome_assembly"],
                    record["pipeline_version"],
                    record["run_date"],
                    record["sequencing_type"],
                    record["qc_status"],
                    record["qc_tss_enrichment_score"],
                    record["qc_frip_score"],
                    record["qc_library_complexity"],
                    record["qc_mito_reads_percent"],
                    record["qc_total_peaks_called"],
                    record["qc_duplicate_rate"],
                    record["qc_mapped_reads"],
                    record["qc_fragment_size_median"],
                )
                try:
                    cursor.execute(
                        """
                        INSERT INTO atacseq_sample_table(
                            sample_id,
                            genome_assembly,
                            pipeline_version,
                            run_date,
                            sequencing_type,
                            qc_status,
                            qc_tss_enrichment_score,
                            qc_frip_score,
                            qc_library_complexity,
                            qc_mito_reads_percent,
                            qc_total_peaks_called,
                            qc_duplicate_rate,
                            qc_mapped_reads,
                            qc_fragment_size_median
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """,
                        row,
                    )
                except psycopg2.Error as e:
                    print(f"Error inserting ATAC-seq sample '{sample_id}': {e}")
                    raise

        conn.commit()
        print("ATAC-seq pipeline outputs populated.")
    except Exception:
        conn.rollback()
        raise


def chipseq_sample_metadata(conn, sample):
    """Populate the output features table for ChIP-seq pipeline results."""
    required_keys = [
        "genome_assembly", "spikein_genome", "pipeline_version", "run_date",
        "qc_status", "qc_mapped_reads", "qc_mito_reads_percent",
        "qc_duplicate_rate", "qc_fragment_size_median", "qc_library_complexity",
        "qc_spikein_scaling_called", "qc_total_peaks_called"
    ]
    _validate_inputs(conn, sample, required_keys=required_keys)

    try:
        with conn.cursor() as cursor:
            for sample_id, record in sample.items():
                row = (
                    sample_id,
                    record["genome_assembly"],
                    record["spikein_genome"],
                    record["pipeline_version"],
                    record["run_date"],
                    record["qc_status"],
                    record["qc_mapped_reads"],
                    record["qc_mito_reads_percent"],
                    record["qc_duplicate_rate"],
                    record["qc_fragment_size_median"],
                    record["qc_library_complexity"],
                    record["qc_spikein_scaling_called"],
                    record["qc_total_peaks_called"],
                )
                try:
                    cursor.execute(
                        """
                        INSERT INTO chipseq_sample_table(
                            sample_id,
                            genome_assembly,
                            spikein_genome,
                            pipeline_version,
                            run_date,
                            qc_status,
                            qc_mapped_reads,
                            qc_mito_reads_percent,
                            qc_duplicate_rate,
                            qc_fragment_size_median,
                            qc_library_complexity,
                            qc_spikein_scaling_called,
                            qc_total_peaks_called
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """,
                        row,
                    )
                except psycopg2.Error as e:
                    print(f"Error inserting ChIP-seq sample '{sample_id}': {e}")
                    raise

        conn.commit()
        print("ChIP-seq pipeline outputs populated.")
    except Exception:
        conn.rollback()
        raise


def cut_and_run_sample_metadata(conn, sample):
    """Populate the output features table for CUT&RUN pipeline results."""
    required_keys = [
        "genome_assembly", "pipeline_version", "run_date", "mito_chr",
        "mapq_threshold", "macs2_qvalue", "qc_status", "qc_mapped_reads",
        "qc_alignment_rate", "qc_mito_reads_percent", "qc_duplicate_rate",
        "qc_fragment_size_median", "qc_frip_score", "qc_nsc_coefficient",
        "qc_rsc_coefficient", "qc_estimated_fragment_length",
        "qc_library_complexity", "qc_total_peaks_called",
        "qc_peaks_after_blacklist_filter"
    ]
    _validate_inputs(conn, sample, required_keys=required_keys)

    try:
        with conn.cursor() as cursor:
            for sample_id, record in sample.items():
                row = (
                    sample_id,
                    record["genome_assembly"],
                    record["pipeline_version"],
                    record["run_date"],
                    record["mito_chr"],
                    record["mapq_threshold"],
                    record["macs2_qvalue"],
                    record["qc_status"],
                    record["qc_mapped_reads"],
                    record["qc_alignment_rate"],
                    record["qc_mito_reads_percent"],
                    record["qc_duplicate_rate"],
                    record["qc_fragment_size_median"],
                    record["qc_frip_score"],
                    record["qc_nsc_coefficient"],
                    record["qc_rsc_coefficient"],
                    record["qc_estimated_fragment_length"],
                    record["qc_library_complexity"],
                    record["qc_total_peaks_called"],
                    record["qc_peaks_after_blacklist_filter"],
                )
                try:
                    cursor.execute(
                        """
                        INSERT INTO cut_and_run_sample_metadata_table(
                            sample_id,
                            genome_assembly,
                            pipeline_version,
                            run_date,
                            mito_chr,
                            mapq_threshold,
                            macs2_qvalue,
                            qc_status,
                            qc_mapped_reads,
                            qc_alignment_rate,
                            qc_mito_reads_percent,
                            qc_duplicate_rate,
                            qc_fragment_size_median,
                            qc_frip_score,
                            qc_nsc_coefficient,
                            qc_rsc_coefficient,
                            qc_estimated_fragment_length,
                            qc_library_complexity,
                            qc_total_peaks_called,
                            qc_peaks_after_blacklist_filter
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """,
                        row,
                    )
                except psycopg2.Error as e:
                    print(f"Error inserting CUT&RUN sample '{sample_id}': {e}")
                    raise

        conn.commit()
        print("CUT&RUN pipeline outputs populated.")
    except Exception:
        conn.rollback()
        raise


def rnaseq_sample_metadata(conn, sample):
    """Populate the output features table for RNA-seq pipeline results."""
    required_keys = [
        "genome_assembly", "pipeline_version", "run_date", "star_sjdb_overhang",
        "qc_status", "qc_mapped_reads", "qc_alignment_rate", "qc_duplicate_rate",
        "qc_median_insert_size", "qc_library_complexity", "qc_assigned_reads",
        "qc_assignment_rate", "qc_exonic_rate", "qc_intronic_rate",
        "qc_intergenic_rate", "qc_rrna_percent", "qc_gene_body_3prime_bias",
        "qc_strand_specificity", "qc_junction_reads",
        "qc_junction_annotation_rate", "qc_gc_bias"
    ]
    _validate_inputs(conn, sample, required_keys=required_keys)

    try:
        with conn.cursor() as cursor:
            for sample_id, record in sample.items():
                row = (
                    sample_id,
                    record["genome_assembly"],
                    record["pipeline_version"],
                    record["run_date"],
                    record["star_sjdb_overhang"],
                    record["qc_status"],
                    record["qc_mapped_reads"],
                    record["qc_alignment_rate"],
                    record["qc_duplicate_rate"],
                    record["qc_median_insert_size"],
                    record["qc_library_complexity"],
                    record["qc_assigned_reads"],
                    record["qc_assignment_rate"],
                    record["qc_exonic_rate"],
                    record["qc_intronic_rate"],
                    record["qc_intergenic_rate"],
                    record["qc_rrna_percent"],
                    record["qc_gene_body_3prime_bias"],
                    record["qc_strand_specificity"],
                    record["qc_junction_reads"],
                    record["qc_junction_annotation_rate"],
                    record["qc_gc_bias"],
                )
                try:
                    cursor.execute(
                        """
                        INSERT INTO rnaseq_sample_table(
                            sample_id,
                            genome_assembly,
                            pipeline_version,
                            run_date,
                            star_sjdb_overhang,
                            qc_status,
                            qc_mapped_reads,
                            qc_alignment_rate,
                            qc_duplicate_rate,
                            qc_median_insert_size,
                            qc_library_complexity,
                            qc_assigned_reads,
                            qc_assignment_rate,
                            qc_exonic_rate,
                            qc_intronic_rate,
                            qc_intergenic_rate,
                            qc_rrna_percent,
                            qc_gene_body_3prime_bias,
                            qc_strand_specificity,
                            qc_junction_reads,
                            qc_junction_annotation_rate,
                            qc_gc_bias
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """,
                        row,
                    )
                except psycopg2.Error as e:
                    print(f"Error inserting RNA-seq sample '{sample_id}': {e}")
                    raise

        conn.commit()
        print("RNA-seq pipeline outputs populated.")
    except Exception:
        conn.rollback()
        raise


def sample_sheet_metadata(conn, sample):
    """Populate the sample sheet metadata table."""
    required_keys = [
        "replicate", "condition", "fastq_r1", "fastq_r2"
    ]
    _validate_inputs(conn, sample, required_keys=required_keys)

    try:
        with conn.cursor() as cursor:
            for sample_id, record in sample.items():
                row = (
                    sample_id,
                    record["replicate"],
                    record["condition"],
                    record["fastq_r1"],
                    record["fastq_r2"],
                    record.get("control_sample_id"),
                )
                try:
                    cursor.execute(
                        """
                        INSERT INTO sample_sheet_metadata(
                            sample_id,
                            replicate,
                            condition,
                            fastq_r1,
                            fastq_r2,
                            control_sample_id
                        )
                        VALUES (%s, %s, %s, %s, %s, %s)
                        """,
                        row,
                    )
                except psycopg2.Error as e:
                    print(f"Error inserting sample sheet metadata '{sample_id}': {e}")
                    raise

        conn.commit()
        print("Sample sheet metadata populated.")
    except Exception:
        conn.rollback()
        raise
ple_id}': {e}")
                    raise

        conn.commit()
        print("Sample sheet metadata populated.")
    except Exception:
        conn.rollback()
        raise
