from flask import Flask
from flask.ext import restful

from api_v1 import Server, ServerList, Channel, ChannelList

app = Flask(__name__)
app.config.from_object('config')

api_v1 = restful.Api(app)

# Servers
api_v1.add_resource(ServerList, '/v1/servers/')
api_v1.add_resource(Server, '/v1/servers/<int:server_id>/')
api_v1.add_resource(ChannelList, '/v1/servers/<int:server_id>/channels/')
api_v1.add_resource(Channel, '/v1/servers/<int:server_id>/channels/<int:channel_id>/')
