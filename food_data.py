from __future__ import annotations
from typing import Any, Optional
from pydantic import BaseModel
import configparser
import requests as rq
import re


class NutritionalData(BaseModel):
    old_api_id: Optional[Any] = None
    item_id: Optional[str] = None
    item_name: Optional[str] = None
    leg_loc_id: Optional[Any] = None
    brand_id: Optional[str] = None
    brand_name: Optional[str] = None
    item_description: Optional[Any] = None
    updated_at: Optional[str] = None
    nf_ingredient_statement: Optional[str] = None
    nf_water_grams: Optional[Any] = None
    nf_calories: Optional[int] = None
    nf_calories_from_fat: Optional[int] = None
    nf_total_fat: Optional[int] = None
    nf_saturated_fat: Optional[int] = None
    nf_trans_fatty_acid: Optional[int] = None
    nf_polyunsaturated_fat: Optional[float] = None
    nf_monounsaturated_fat: Optional[int] = None
    nf_cholesterol: Optional[int] = None
    nf_sodium: Optional[int] = None
    nf_total_carbohydrate: Optional[int] = None
    nf_dietary_fiber: Optional[int] = None
    nf_sugars: Optional[int] = None
    nf_protein: Optional[int] = None
    nf_vitamin_a_dv: Optional[Any] = None
    nf_vitamin_c_dv: Optional[Any] = None
    nf_calcium_dv: Optional[float] = None
    nf_iron_dv: Optional[float] = None
    nf_refuse_pct: Optional[Any] = None
    nf_servings_per_container: Optional[int] = None
    nf_serving_size_qty: Optional[int] = None
    nf_serving_size_unit: Optional[str] = None
    nf_serving_weight_grams: Optional[int] = None
    allergen_contains_milk: Optional[Any] = None
    allergen_contains_eggs: Optional[Any] = None
    allergen_contains_fish: Optional[Any] = None
    allergen_contains_shellfish: Optional[Any] = None
    allergen_contains_tree_nuts: Optional[Any] = None
    allergen_contains_peanuts: Optional[Any] = None
    allergen_contains_wheat: Optional[Any] = None
    allergen_contains_soybeans: Optional[Any] = None
    allergen_contains_gluten: Optional[Any] = None
    usda_fields: Optional[Any] = None


class NutritionalAPI:
    def __init__(self, upc_code: str) -> None:
        config = configparser.ConfigParser()
        config.read("config.ini")
        self._url = config["API"]["Url"]
        self._host = config["API"]["Host"]
        self._key = config["API"]["Key"]
        self._headers = {"X-RapidAPI-Key": self._key, "X-RapidAPI-Host": self._host}
        self.upc_code = upc_code
        self._querystring = {"upc": self._upc_code}

    @property
    def upc_code(self):
        return self._upc_code

    @upc_code.setter
    def upc_code(self, value):
        if bool(re.search(r"\D", value)):
            raise ValueError("UPC Code can only include numbers")
        elif len(value) == 10 or len(value) == 12:
            self._upc_code = value
        else:
            raise ValueError("UPC code must be 10 or 12 characters")

    @property
    def data(self) -> NutritionalData:

        response = rq.get(
            self._url, headers=self._headers, params=self._querystring
        ).json()

        return NutritionalData(**response)
