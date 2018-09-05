from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from .domain import Client, PU, Metric, serviceNames




class ClientSchema(ModelSchema):
  pus = fields.Nested("PUSchema", many = True, exclude = ("metrics"))
  class Meta:
      model = Client


class PUSchema(ModelSchema):
  serviceName = fields.Method('getServiceName')
  class Meta:
      model = PU

  def getServiceName(self, pu):
    return serviceNames[pu.getService()]


class MetricSchema(ModelSchema):
  pu = fields.Nested("PUSchema", exclude = ("client"))
  m = fields.Method('getM')
  class Meta:
      model = Metric

  def getM(self, metric):
    return metric.m.split(";")



clientSchema = ClientSchema()
clientsSchema = ClientSchema(many = True)
metricsSchema = MetricSchema(many = True)