from megaparse.parser.strategy import determine_strategy
from megaparse_sdk.schema.parser_config import StrategyEnum


def test_strategy_all():
    pdf = "./tests/pdf/sample_pdf.pdf"
    strategy = determine_strategy(
        pdf, threshold_pages_ocr=0.2, threshold_image_page=0.3
    )
    assert strategy == StrategyEnum.HI_RES
