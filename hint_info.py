from datetime import datetime


class RecommendAdvice():
    def __init__(self, requested_ticker):
        self.reg_ticker = requested_ticker
        self.tickers_list = ['AAPL', 'F', 'MSFT', 'BABA']  # текущий рабочий список опций для запроса


    def SummarizeAnswer(self):
        # analytic_operations here...

        if self.reg_ticker[0] not in self.tickers_list:
            print(f'self.reg_ticker: {self.reg_ticker} ; self.tickers_list: {self.tickers_list}; {self.reg_ticker[0] in self.tickers_list}')
            pass
        else:
            part_1 = f'сегодн, {datetime.now().date()}, даю описание компании {self.reg_ticker[0]}...\n'
            part_2 = f'Фундаментальные данные компании {self.reg_ticker[0]}...\n'
            part_3 = f'Тех.данные компании {self.reg_ticker[0]}...\n'

            summary = [part_1, part_2, part_3]
            return summary
