import json
from ad_api.api.reports.base_report import Base


class Adgroup(Base):
    """Sponsored Products Adgroup Reports
    
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
        cols = cols if cols else ["campaignId",
                                    "campaignName",
                                    "campaignStatus",
                                    "campaignBudgetAmount",
                                    "campaignBudgetType",
                                    "adGroupId",
                                    "adGroupName",
                                    "adStatus",
                                    "date",
                                    "impressions",
                                    "clicks",
                                    "cost",
                                    "costPerClick",
                                    "clickThroughRate",
                                    "spend",
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
                                    "attributedSalesSameSku1d",
                                    "attributedSalesSameSku7d",
                                    "attributedSalesSameSku14d",
                                    "attributedSalesSameSku30d",
                                    "unitsSoldSameSku1d",
                                    "unitsSoldSameSku7d",
                                    "unitsSoldSameSku14d",
                                    "unitsSoldSameSku30d",
                                  ]
        body = {
            "name": "SP adgroups report",
            "startDate": start_date,
            "endDate": end_date,
            "configuration": {
                "adProduct": "SPONSORED_PRODUCTS",
                "groupBy": ["adGroup", "campaign"],
                "columns": cols,
                "reportTypeId": "spCampaigns",
                "timeUnit": time_unit,
                "format": "GZIP_JSON"
            }
        }
        return self._generate_report(body, filters)

