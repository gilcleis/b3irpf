import copy
import datetime


class Event:
	def __init__(self, title: str,
	             quantity: float = 0.0,
	             value: float = 0.0):
		self.title = title
		self.quantity = quantity
		self.value = value
		self.items = []

	def __str__(self):
		return self.title


class Credit(dict):
	"""credito"""


class Debit(dict):
	"""Débito"""


class Events(dict):
	"""Eventos"""


class Buy:
	"""Compas"""

	def __init__(self, quantity: float = 0,
	             avg_price: float = 0.0,
	             total: float = 0.0,
	             tax: float = 0.0,
	             date: datetime.date = None):
		self.quantity = quantity
		self.avg_price = avg_price
		self.total = total
		self.tax = tax
		self.date = date


class Sell:
	"""Vendas"""

	def __init__(self, quantity: float = 0,
	             avg_price: float = 0.0,
	             total: float = 0.0,
	             capital: float = 0.0,
	             tax: float = 0.0,
	             date: datetime.date = None):
		self.quantity = quantity
		self.avg_price = avg_price
		self.capital = capital
		self.total = total
		self.tax = tax
		self.date = date

	def __bool__(self):
		return bool(self.quantity)


class Period:
	"""Compas menos vendas no intervalo de tempo"""

	def __init__(self, quantity: float = 0,
	             avg_price: float = 0.0,
	             total: float = 0.0,
	             tax: float = 0.0,
	             position=None):
		self.quantity = quantity
		self.avg_price = avg_price
		self.position = position
		self.total = total
		self.tax = tax


class Asset:
	"""Ativos"""

	def __init__(self, ticker,
	             buy: Buy = None, sell: Sell = None,
	             position=None,
	             credit: Credit = None,
	             debit: Debit = None,
	             events: Events = None,
	             institution=None,
	             enterprise=None):
		self.items = []
		self.ticker = ticker
		self.buy = buy
		self.sell = sell
		self.position = position
		self.credit = credit
		self.debit = debit
		self.events = events
		self.institution = institution
		self.enterprise = enterprise

		if buy is None:
			self.buy = Buy()
		if sell is None:
			self.sell = Sell()
		if credit is None:
			self.credit = Credit()
		if debit is None:
			self.debit = Debit()
		if events is None:
			self.events = Events()

	@property
	def period(self) -> Period:
		"""Compras menos vendas no intervalo de tempo"""
		quantity = self.buy.quantity - self.sell.quantity
		total = quantity * ((self.buy.total / quantity) if quantity > 0.0 else 0.0)
		avg_price = (total / quantity) if quantity > 0 else 0.0
		try:
			# 5.0 % 5 == 0, 5.5 % 5 = 0.5
			if quantity % quantity == 0:
				# converte para inteiro porque o valor não tem fração relevante
				quantity = int(quantity)
		except ZeroDivisionError:
			...
		period = Period(quantity=quantity,
		                avg_price=avg_price,
		                total=total,
		                tax=self.buy.tax,
		                position=self.position)
		return period

	def __deepcopy__(self, memo):
		memo[id(self)] = cpy = type(self)(
			ticker=self.ticker,
			buy=copy.deepcopy(self.buy, memo),
			sell=copy.deepcopy(self.sell, memo),
			credit=copy.deepcopy(self.credit, memo),
			debit=copy.deepcopy(self.debit, memo),
			events=copy.deepcopy(self.events, memo),
			institution=self.institution,
			enterprise=self.enterprise,
			position=self.position
		)
		return cpy

	def __iter__(self):
		return iter(self.items)

