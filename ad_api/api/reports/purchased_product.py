import json
from ad_api.api.reports.base_report import Base


class PurchasedProduct(Base):
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
            "adGroupId",
            "adGroupName",
            "keywordId",
            "keyword",
            "keywordType",
            "matchType",
            "portfolioId",
            "advertisedAsin",
            "purchasedAsin",
            "advertisedSku",
            "date",
            "unitsSoldClicks1d",
            "unitsSoldClicks7d",
            "unitsSoldClicks14d",
            "unitsSoldClicks30d",
            "sales1d",
            "sales7d",
            "sales14d",
            "sales30d",
            "purchases1d",
            "purchases7d",
            "purchases14d",
            "purchases30d",
            "unitsSoldOtherSku1d",
            "unitsSoldOtherSku7d",
            "unitsSoldOtherSku14d",
            "unitsSoldOtherSku30d",
            "salesOtherSku1d",
            "salesOtherSku7d",
            "salesOtherSku14d",
            "salesOtherSku30d",
            "purchasesOtherSku1d",
            "purchasesOtherSku7d",
            "purchasesOtherSku14d",
            "purchasesOtherSku30d",
        ]

        body = {
            "name": "SP campaigns report",
            "startDate": start_date,
            "endDate": end_date,
            "configuration": {
                "adProduct": "SPONSORED_PRODUCTS",
                "groupBy": ['asin'],
                "columns": cols,
                "reportTypeId": "spPurchasedProduct",
                "timeUnit": time_unit,
                "format": "GZIP_JSON"
            }
        }
        return self._generate_report(body, filters)

