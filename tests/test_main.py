import os
from unittest.mock import patch

import pandas as pd
import pytest

# Add the project root directory to the Python path to fix import issues
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dataslicer.main import main


@pytest.fixture
def temp_csv(tmp_path):
    """Creates a temporary CSV file with test data."""
    temp_file = tmp_path / "test_file.csv"
    test_content = """Name,Department,Salary
Alice,HR,50000
Bob,IT,60000
Charlie,HR,55000
David,IT,70000
"""
    temp_file.write_text(test_content)
    return str(temp_file)


@pytest.fixture
def temp_excel(tmp_path):
    """Creates a temporary Excel file with test data."""
    temp_file = tmp_path / "test_file.xlsx"
    df = pd.DataFrame(
        {
            "Name": ["Alice", "Bob", "Charlie", "David"],
            "Department": ["HR", "IT", "HR", "IT"],
            "Salary": [50000, 60000, 55000, 70000],
        }
    )
    df.to_excel(temp_file, index=False)
    return str(temp_file)


def test_main_csv_workflow(temp_csv, tmp_path, monkeypatch):
    """Test the complete workflow of main() with CSV input and output."""
    export_folder = str(tmp_path / "exports")
    os.makedirs(export_folder, exist_ok=True)

    # Mock the inputs using patch for input function
    with patch(
        "builtins.input",
        side_effect=[
            temp_csv,  # file path
            "2",  # select Department column
            "",  # finish column selection
            "2",  # select Department for filename
            export_folder,  # export folder
            "2",  # choose CSV format
        ],
    ):
        # Run the main function
        main()

    # Check that the expected files were created
    hr_file = os.path.join(export_folder, "HR", "HR.csv")
    it_file = os.path.join(export_folder, "IT", "IT.csv")

    assert os.path.exists(hr_file), f"HR file was not created at {hr_file}"
    assert os.path.exists(it_file), f"IT file was not created at {it_file}"

    # Verify content of HR file
    hr_df = pd.read_csv(hr_file)
    assert len(hr_df) == 2
    assert "Alice" in list(hr_df["Name"]) and "Charlie" in list(hr_df["Name"])

    # Verify content of IT file
    it_df = pd.read_csv(it_file)
    assert len(it_df) == 2
    assert "Bob" in list(it_df["Name"]) and "David" in list(it_df["Name"])


def test_main_excel_workflow(temp_excel, tmp_path, monkeypatch):
    """Test the complete workflow of main() with Excel input and output."""
    export_folder = str(tmp_path / "exports_excel")
    os.makedirs(export_folder, exist_ok=True)

    # Mock the inputs using patch for input function
    with patch(
        "builtins.input",
        side_effect=[
            temp_excel,  # file path
            "2",  # select Department column
            "",  # finish column selection
            "2",  # select Department for filename
            export_folder,  # export folder
            "1",  # choose Excel format
        ],
    ):
        # Run the main function
        main()

    # Check that the expected files were created
    hr_file = os.path.join(export_folder, "HR", "HR.xlsx")
    it_file = os.path.join(export_folder, "IT", "IT.xlsx")

    assert os.path.exists(hr_file), f"HR file was not created at {hr_file}"
    assert os.path.exists(it_file), f"IT file was not created at {it_file}"

    # Verify content of HR file
    hr_df = pd.read_excel(hr_file)
    assert len(hr_df) == 2
    assert "Alice" in list(hr_df["Name"]) and "Charlie" in list(hr_df["Name"])

    # Verify content of IT file
    it_df = pd.read_excel(it_file)
    assert len(it_df) == 2
    assert "Bob" in list(it_df["Name"]) and "David" in list(it_df["Name"])


def test_main_with_custom_filename(temp_csv, tmp_path, monkeypatch):
    """Test the workflow with a custom filename option."""
    export_folder = str(tmp_path / "exports_custom")
    os.makedirs(export_folder, exist_ok=True)

    # Mock the inputs using patch for input function
    with patch(
        "builtins.input",
        side_effect=[
            temp_csv,  # file path
            "2",  # select Department column
            "",  # finish column selection
            "0",  # select custom filename
            "test_export",  # custom filename
            export_folder,  # export folder
            "2",  # choose CSV format
        ],
    ):
        # Run the main function
        main()

    # Check that the expected files were created
    hr_file = os.path.join(export_folder, "HR", "test_export.csv")
    it_file = os.path.join(export_folder, "IT", "test_export.csv")

    assert os.path.exists(hr_file), f"HR file was not created at {hr_file}"
    assert os.path.exists(it_file), f"IT file was not created at {it_file}"


def test_main_with_multiple_group_columns(temp_csv, tmp_path, monkeypatch):
    """Test grouping by multiple columns."""
    export_folder = str(tmp_path / "exports_multi")
    os.makedirs(export_folder, exist_ok=True)

    # Mock the inputs using patch for input function
    with patch(
        "builtins.input",
        side_effect=[
            temp_csv,  # file path
            "1",  # select Name column (index 1 initially)
            "1",  # select Department column (now index 1 after Name was removed)
            "",  # finish column selection
            "3",  # select Salary for filename (now index 1 in remaining columns)
            export_folder,  # export folder
            "2",  # choose CSV format
        ],
    ):
        # Run the main function
        main()

    # Check that the expected nested folder structure was created
    # With Name then Department grouping, and using Salary for filename
    paths = [
        os.path.join(export_folder, "Alice", "HR", "50000.csv"),
        os.path.join(export_folder, "Bob", "IT", "60000.csv"),
        os.path.join(export_folder, "Charlie", "HR", "55000.csv"),
        os.path.join(export_folder, "David", "IT", "70000.csv"),
    ]

    for path in paths:
        assert os.path.exists(path), f"File was not created at {path}"
