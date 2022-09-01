import json
from ad_api.api.reports.base_report import Base


class TargetingExpression(Base):
    """Sponsored Products Reports
    
    Documentation: https://advertising.amazon.com/API/docs/en-us/reporting/v3/overview
    
    Use the Amazon Advertising API for Sponsored Products for campaign, ad group, keyword/targeting, search term, negative keyword, and product ad management operations. For more information about Sponsored Products, see the Sponsored Products Support Center. For onboarding information, see the account setup topic.
    """

    def generate_report(self, start_date, end_date, cols=None, filters=None, time_unit='DAILY'):
        """
        generate reports
        Args:
            cols (list): columns list
            start_date (str): date string format: YYYY-mm-dd
            end_date (str): date string format: YYYY-mm-dd
            filters (dict): filter dict
            time_unit (str): 'DAILY' or 'SUMMARY'
        """
        cols = cols if cols else [
            "campaignId",
            "campaignName",
            "campaignStatus",
            "campaignBudgetAmount",
            "campaignBudgetType",
            "portfolioId",
            "adGroupId",
            "adGroupName",
            "keywordId",
            "keyword",
            "keywordBid",
            "keywordType",
            "matchType",
            "targeting",
            "adKeywordStatus",
            "date",
            "impressions",
            "clicks",
            "cost",
            "costPerClick",
            "clickThroughRate",
            "purchases1d",
            "purchases7d",
            "purchases14d",
            "purchases30d",
            "purchasesSameSku1d",
            "purchasesSameSku7d",
            "purchasesSameSku14d",
            "purchasesSameSku30d",
            "unitsSoldClicks1d",
            "unitsSoldClicks7d",
            "unitsSoldClicks14d",
            "unitsSoldClicks30d",
            "sales1d",
            "sales7d",
            "sales14d",
            "sales30d",
            "salesOtherSku7d",
            "attributedSalesSameSku1d",
            "attributedSalesSameSku7d",
            "attributedSalesSameSku14d",
            "attributedSalesSameSku30d",
            "unitsSoldSameSku1d",
            "unitsSoldSameSku7d",
            "unitsSoldSameSku14d",
            "unitsSoldSameSku30d",
            "unitsSoldOtherSku7d",
            "acosClicks7d",
            "acosClicks14d",
            "roasClicks7d",
            "roasClicks14d",
        ]

        body = {
            "name": "SP campaigns report",
            "startDate": start_date,
            "endDate": end_date,
            "configuration": {
                "adProduct": "SPONSORED_PRODUCTS",
                "groupBy": ['targeting'],
                "columns": cols,
                "filters": [
                    {
                        "field": "keywordType",
                        "values": [
                            "TARGETING_EXPRESSION",
                            "TARGETING_EXPRESSION_PREDEFINED"
                        ]
                    }
                ],
                "reportTypeId": "spTargeting",
                "timeUnit": time_unit,
                "format": "GZIP_JSON"
            }
        }
        return self._generate_report(body, filters)

