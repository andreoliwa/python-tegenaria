"""Marshmallow schemas."""
from typing import Any, Dict

from marshmallow.decorators import pre_load
from marshmallow_sqlalchemy import ModelSchema

from tegenaria.extensions import db
from tegenaria.models import Apartment
from tegenaria.spiders import SpiderMixin


class ApartmentSchema(ModelSchema):
    """Schema to represent an apartment."""

    class Meta:
        """Schema config."""

        model = Apartment
        sqla_session = db.session

    @pre_load
    def clean_item(self, data: Dict[str, Any]):
        """Clean the item before loading schema on Marshmallow."""
        spider = self.context["spider"]  # type: SpiderMixin
        return spider.before_marshmallow(data)
