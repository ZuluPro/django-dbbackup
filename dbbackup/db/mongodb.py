from .base import BaseCommandDBConnector


class MongoDumpConnector(BaseCommandDBConnector):
    """
    MongoDB connector, creates dump with ``mongodump`` and restore with
    ``mongorestore``.
    """
    dump_cmd = 'mongodump'
    restore_cmd = 'mongorestore'
    object_check = True
    drop = True

    def create_dump(self):
        cmd = '%s --db %s' % (self.dump_cmd, self.settings['NAME'])
        cmd += ' --host %s:%s' % (self.settings['HOST'], self.settings['PORT'])
        if 'USER' in self.settings:
            cmd += ' --username %s' % self.settings['USER']
        if 'PASSWORD' in self.settings:
            cmd += ' --password %s' % self.settings['PASSWORD']
        for collection in self.exclude:
            cmd += ' --excludeCollection %s' % collection
        cmd += ' --archive'
        return self.run_command(cmd)

    def restore_dump(self, dump):
        cmd = self.restore_cmd
        cmd += ' --host %s:%s' % (self.settings['HOST'], self.settings['PORT'])
        if 'USER' in self.settings:
            cmd += ' --username %s' % self.settings['USER']
        if 'PASSWORD' in self.settings:
            cmd += ' --password %s' % self.settings['PASSWORD']
        if self.object_check:
            cmd += ' --objcheck'
        if self.drop:
            cmd += ' --drop'
        cmd += ' --archive'
        return self.run_command(cmd, stdin=dump)
