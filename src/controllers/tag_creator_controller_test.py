from unittest.mock import patch
from src.drivers.barcode_handler import BarcodeHandler
from .tag_creator_controller import TagCreatorController


@patch.object(BarcodeHandler, "create_barcode")
def test_create(mock_create_barcode):
    mock_value = "image_path"
    mock_create_barcode.return_value = mock_value
    result = TagCreatorController().create(product_code=mock_value)

    assert isinstance(result, dict)

    assert "data" in result
    assert "type" in result["data"]
    assert result["data"]["type"] == "Tag image"
    assert "count" in result["data"]
    assert result["data"]["count"] == 1
    assert "path" in result["data"]
    assert result["data"]["path"] == f"{mock_value}.png"