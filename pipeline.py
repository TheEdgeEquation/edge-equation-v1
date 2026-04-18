from ingestion.sources import MLBSource, NBASource, NHLSource
from normalization import normalize_records


def run_pipeline():
    sources = [MLBSource(), NBASource(), NHLSource()]
    output = {}

    for src in sources:
        raw = src.fetch()
        normalized = normalize_records(raw)
        output[src.sport] = normalized

    return output


if __name__ == "__main__":
    data = run_pipeline()
    print("Pipeline output:")
    print(data)
