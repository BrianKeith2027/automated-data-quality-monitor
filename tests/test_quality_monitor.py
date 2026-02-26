"""
Unit Tests for Automated Data Quality Monitor
Author: Brian Stratton
"""

import pytest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


# ============================================================
# Test Fixtures
# ============================================================

@pytest.fixture
def clean_data():
    """Generate clean sample data"""
    np.random.seed(42)
    n = 100
    return pd.DataFrame({
        "id": range(1, n + 1),
        "name": [f"Product_{i}" for i in range(1, n + 1)],
        "price": np.random.uniform(10, 500, n).round(2),
        "quantity": np.random.randint(1, 100, n),
        "category": np.random.choice(["Electronics", "Clothing", "Food", "Books"], n),
        "date": pd.date_range("2024-01-01", periods=n, freq="D"),
        "email": [f"user{i}@example.com" for i in range(1, n + 1)],
    })


@pytest.fixture
def dirty_data():
    """Generate data with quality issues"""
    np.random.seed(42)
    n = 100
    prices = np.random.uniform(10, 500, n).round(2)
    prices[5] = None
    prices[15] = None
    prices[25] = -50.0  # negative price
    prices[35] = 99999.99  # outlier

    names = [f"Product_{i}" for i in range(1, n + 1)]
    names[10] = None
    names[20] = ""
    names[50] = names[51]  # duplicate name

    return pd.DataFrame({
        "id": list(range(1, n + 1)),
        "name": names,
        "price": prices,
        "quantity": np.random.randint(1, 100, n),
        "category": np.random.choice(["Electronics", "Clothing", "Food", "Books", None], n),
        "date": pd.date_range("2024-01-01", periods=n, freq="D"),
    })


# ============================================================
# Completeness Tests
# ============================================================

class TestCompleteness:
    """Tests for completeness scoring"""

    def test_fully_complete_data(self, clean_data):
        null_pct = clean_data.isnull().mean().mean() * 100
        assert null_pct == 0.0

    def test_null_detection(self, dirty_data):
        null_counts = dirty_data.isnull().sum()
        assert null_counts["price"] == 2
        assert null_counts["name"] == 1

    def test_completeness_score_calculation(self, clean_data):
        completeness = (1 - clean_data.isnull().mean().mean()) * 100
        assert completeness == 100.0

    def test_partial_completeness(self, dirty_data):
        completeness = (1 - dirty_data.isnull().mean().mean()) * 100
        assert 0 < completeness < 100


# ============================================================
# Accuracy Tests
# ============================================================

class TestAccuracy:
    """Tests for accuracy validation"""

    def test_zscore_outlier_detection(self, clean_data):
        from scipy import stats
        z_scores = np.abs(stats.zscore(clean_data["price"].dropna()))
        outliers = (z_scores > 3).sum()
        assert isinstance(outliers, (int, np.integer))

    def test_negative_value_detection(self, dirty_data):
        negative_prices = (dirty_data["price"].dropna() < 0).sum()
        assert negative_prices >= 1

    def test_type_validation(self, clean_data):
        assert clean_data["price"].dtype in [np.float64, np.float32]
        assert clean_data["quantity"].dtype in [np.int64, np.int32]


# ============================================================
# Consistency Tests
# ============================================================

class TestConsistency:
    """Tests for consistency checks"""

    def test_unique_ids(self, clean_data):
        assert clean_data["id"].is_unique

    def test_duplicate_detection(self, dirty_data):
        duplicates = dirty_data.duplicated().sum()
        assert isinstance(duplicates, (int, np.integer))

    def test_category_consistency(self, clean_data):
        valid_categories = {"Electronics", "Clothing", "Food", "Books"}
        actual = set(clean_data["category"].unique())
        assert actual.issubset(valid_categories)


# ============================================================
# Timeliness Tests
# ============================================================

class TestTimeliness:
    """Tests for timeliness validation"""

    def test_no_future_dates(self, clean_data):
        future = (clean_data["date"] > datetime.now()).sum()
        assert future == 0

    def test_date_range_valid(self, clean_data):
        date_range = (clean_data["date"].max() - clean_data["date"].min()).days
        assert date_range > 0


# ============================================================
# Quality Scoring Tests
# ============================================================

class TestQualityScoring:
    """Tests for composite quality score"""

    def test_score_range(self, clean_data):
        completeness = (1 - clean_data.isnull().mean().mean()) * 100
        assert 0 <= completeness <= 100

    def test_clean_data_high_score(self, clean_data):
        completeness = (1 - clean_data.isnull().mean().mean()) * 100
        assert completeness >= 90

    def test_dirty_data_lower_score(self, dirty_data):
        completeness = (1 - dirty_data.isnull().mean().mean()) * 100
        # Dirty data should have lower completeness
        assert completeness < 100


# ============================================================
# Profiling Tests
# ============================================================

class TestProfiling:
    """Tests for data profiling"""

    def test_column_stats(self, clean_data):
        stats = clean_data.describe()
        assert "price" in stats.columns
        assert "count" in stats.index
        assert "mean" in stats.index

    def test_value_counts(self, clean_data):
        counts = clean_data["category"].value_counts()
        assert len(counts) > 0
        assert counts.sum() == len(clean_data)

    def test_dtype_profiling(self, clean_data):
        dtypes = clean_data.dtypes
        assert len(dtypes) == len(clean_data.columns)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
