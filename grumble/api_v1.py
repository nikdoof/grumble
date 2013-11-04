from flask import current_app
from flask.ext import restful
from mumble.meta import Meta


class MumbleResource(restful.Resource):

    def _get_meta(self):
        print current_app.config['ICE_SECRET']
        return Meta(current_app.config['ICE_SECRET'])

    def _get_server(self, server_id):
        return self._get_meta().get_server(server_id)


class ServerList(MumbleResource):
    def get(self):
        servers = self._get_meta().get_all_servers()
        return [{'id': srv.id, 'name': srv.get_all_conf()['registername'], 'port': srv.get_all_conf()['port'], 'running': srv.running} for srv in servers]

    def post(self):
        new_port = max([int(x.get_all_conf()['port']) for x in self._get_meta().get_all_servers()]) + 1
        srv = self._get_meta().new_server()
        srv.set_conf('port', str(new_port))
        return {'id': srv.id}, 201


class Server(MumbleResource):
    def get(self, server_id):
        server = self._get_server(server_id)
        if server is None:
            return '', 404
        cfg = server.get_all_conf()
        for k in ['certificate', 'key']:
            cfg.pop(k)
        return cfg

    def delete(self, server_id):
        if self._get_server(server_id).delete():
            return '', 204
        return '', 500

    def start(self, server_id):
        if self._get_server(server_id).start():
            return '', 204
        return '', 500

    def stop(self, server_id):
        if self._get_server(server_id).stop():
            return '', 204
        return '', 500


class Channel(MumbleResource):

    def get(self, server_id, channel_id):
        server = self._get_server(server_id)
        if server is None:
            return '', 404
        channel = server.get_channel(channel_id)
        if channel is None:
            return '', 404
        return channel.serialize(), 200


class ChannelList(MumbleResource):

    def get(self, server_id):
        server = self._get_server(server_id)
        if server is None:
            return '', 404
        channels = []
        for channel in server.get_channels():
            raw = channel.serialize()
            channels.append({
                'id': raw['id'],
                'name': raw['name'],
                'parent': raw['parent'],
                'position': raw['position'],
            })
        return channels