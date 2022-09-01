import abc
import json
import logging
from ad_api.api.reports.v3.reports import Reports

logger = logging.getLogger("amazon.api")


class Base:
    """Sponsored Products Reports
    
    Documentation: https://advertising.amazon.com/API/docs/en-us/reporting/v3/overview
    
    Use the Amazon Advertising API for Sponsored Products for campaign, ad group, keyword/targeting, search term, negative keyword, and product ad management operations. For more information about Sponsored Products, see the Sponsored Products Support Center. For onboarding information, see the account setup topic.
    """
    def __init__(self, marketplace, credentials=None, debug=False):
        self.client = Reports(marketplace=marketplace, credentials=credentials, debug=debug)

    @abc.abstractmethod
    def generate_report(self, start_date, end_date, cols=None, filters=None, time_unit='DAILY'):
        """Generate reports and return a dict.

        Returns:
            list: A dicts of report summary.
        """
        raise NotImplementedError()

    def _generate_report(self, body, filters=None):
        if filters:
            if isinstance(filters, list):
                body['configuration']['filters'] += filters
            elif isinstance(filters, dict):
                body['configuration']['filters'].append(filters)

        resp = self.client.post_report(body=json.dumps(body))
        report = resp.payload
        if 'reportId' in report:
            return report['reportId']
        else:
            logger.info(resp)
            return None

    def check_reports(self, report_id):
        resp = self.client.get_report(reportId=report_id)
        report = resp.payload
        if 'status' in report and 'url' in report:
            return report['status'], report['url']
        else:
            return None, None

    def download(self, url):
        return self.client.download_report(url=url, mode='data')


