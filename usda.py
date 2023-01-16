from __future__ import annotations
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
import configparser
import requests as rq


class FoodSearchCriteria(BaseModel):
    query: str
    general_search_input: str = Field(..., alias="generalSearchInput")
    page_number: int = Field(..., alias="pageNumber")
    number_of_results_per_page: int = Field(..., alias="numberOfResultsPerPage")
    page_size: int = Field(..., alias="pageSize")
    require_all_words: bool = Field(..., alias="requireAllWords")


class FoodNutrient(BaseModel):
    nutrient_id: Optional[int] = Field(None, alias="nutrientId")
    nutrient_name: Optional[str] = Field(None, alias="nutrientName")
    nutrient_number: Optional[str] = Field(None, alias="nutrientNumber")
    unit_name: Optional[str] = Field(None, alias="unitName")
    derivation_code: Optional[str] = Field(None, alias="derivationCode")
    derivation_description: Optional[str] = Field(None, alias="derivationDescription")
    derivation_id: Optional[int] = Field(None, alias="derivationId")
    value: Optional[float] = None
    food_nutrient_source_id: Optional[int] = Field(None, alias="foodNutrientSourceId")
    food_nutrient_source_code: Optional[str] = Field(
        None, alias="foodNutrientSourceCode"
    )
    food_nutrient_source_description: Optional[str] = Field(
        None, alias="foodNutrientSourceDescription"
    )
    rank: Optional[int] = None
    indent_level: Optional[int] = Field(None, alias="indentLevel")
    food_nutrient_id: Optional[int] = Field(None, alias="foodNutrientId")
    percent_daily_value: Optional[int] = Field(None, alias="percentDailyValue")


class FoodAttribute(BaseModel):
    value: Optional[str] = None
    name: Optional[str] = None
    id: Optional[int] = None


class FoodAttributeType(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    id: Optional[int] = None
    food_attributes: Optional[List[FoodAttribute]] = Field(None, alias="foodAttributes")


class Food(BaseModel):
    fdc_id: Optional[int] = Field(None, alias="fdcId")
    description: Optional[str]
    lowercase_description: Optional[str] = Field(None, alias="lowercaseDescription")
    data_type: Optional[str] = Field(None, alias="dataType")
    gtin_upc: Optional[str] = Field(None, alias="gtinUpc")
    published_date: Optional[str] = Field(None, alias="publishedDate")
    brand_owner: Optional[str] = Field(None, alias="brandOwner")
    brand_name: Optional[str] = Field(None, alias="brandName")
    ingredients: Optional[str] = None
    market_country: Optional[str] = Field(None, alias="marketCountry")
    food_category: Optional[str] = Field(None, alias="foodCategory")
    modified_date: Optional[str] = Field(None, alias="modifiedDate")
    data_source: Optional[str] = Field(None, alias="dataSource")
    serving_size_unit: Optional[str] = Field(None, alias="servingSizeUnit")
    serving_size: Optional[float] = Field(None, alias="servingSize")
    trade_channels: Optional[List[str]] = Field(None, alias="tradeChannels")
    all_highlight_fields: Optional[str] = Field(None, alias="allHighlightFields")
    score: Optional[float] = None
    microbes: Optional[List] = None
    food_nutrients: Optional[List[FoodNutrient]] = Field(None, alias="foodNutrients")
    final_food_input_foods: Optional[List] = Field(None, alias="finalFoodInputFoods")
    food_measures: Optional[List] = Field(None, alias="foodMeasures")
    food_attributes: Optional[List] = Field(None, alias="foodAttributes")
    food_attribute_types: Optional[List[FoodAttributeType]] = Field(
        None, alias="foodAttributeTypes"
    )
    food_version_ids: Optional[List] = Field(None, alias="foodVersionIds")


class DataType(BaseModel):
    branded: int = Field(..., alias="Branded")
    survey__fndds_: int = Field(..., alias="Survey (FNDDS)")


class Aggregations(BaseModel):
    data_type: DataType = Field(..., alias="dataType")
    nutrients: Dict[str, Any]


class Model(BaseModel):
    total_hits: Optional[int] = Field(None, alias="totalHits")
    current_page: Optional[int] = Field(None, alias="currentPage")
    total_pages: Optional[int] = Field(None, alias="totalPages")
    page_list: Optional[List[int]] = Field(None, alias="pageList")
    food_search_criteria: Optional[FoodSearchCriteria] = Field(
        None, alias="foodSearchCriteria"
    )
    foods: Optional[List[Food]] = None
    aggregations: Optional[Aggregations] = None


class USDA:
    config = configparser.ConfigParser()
    config.read("config.ini")

    api_key = config["USDA"]["Key"]

    url = f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key={api_key}"

    def __init__(self, item, pages) -> None:
        self.item = item
        self.pages = pages

    def get_data(self) -> Model:

        query = {"query": self.item, "pageSize": self.pages}

        data = rq.post(USDA.url, json=query).json()

        return Model(**data)
