from unittest import TestCase
from mock import Mock, patch, sentinel


class DependenciesTests(TestCase):

    def test_getClock(self):
        from scrolls.dependencies import Dependencies
        from scrolls.clock import Clock
        dependencies = Dependencies()
        dependency = dependencies.getClock()
        self.assertIsInstance(dependency, Clock)

    def test_getConfiguration(self):
        from scrolls.dependencies import Dependencies
        from scrolls.configuration import Configuration
        dependencies = Dependencies()
        dependency = dependencies.getConfiguration()
        self.assertIsInstance(dependency, Configuration)

    def test_getCounterFactory(self):
        from scrolls.dependencies import Dependencies
        from scrolls.factories.counter import CounterFactory
        dependencies = Dependencies()
        dependency = dependencies.getCounterFactory()
        self.assertIsInstance(dependency, CounterFactory)

    def test_getFilesystem(self):
        from scrolls.dependencies import Dependencies
        from scrolls.filesystem import Filesystem
        dependencies = Dependencies()
        dependency = dependencies.getFilesystem()
        self.assertIsInstance(dependency, Filesystem)

    def test_getListener(self):
        from scrolls.dependencies import Dependencies
        from scrolls.listener import Listener
        dependencies = Dependencies()
        dependency = dependencies.getListener()
        self.assertIsInstance(dependency, Listener)

    def test_getLog(self):
        from scrolls.dependencies import Dependencies
        from scrolls.log import Log
        dependencies = Dependencies()
        dependency = dependencies.getLog()
        self.assertIsInstance(dependency, Log)

    def test_getMessageFactory(self):
        from scrolls.dependencies import Dependencies
        from scrolls.factories.message import MessageFactory
        dependencies = Dependencies()
        dependency = dependencies.getMessageFactory()
        self.assertIsInstance(dependency, MessageFactory)

    def test_getMessageFactory_passes_request(self):
        from scrolls.dependencies import Dependencies
        with patch('scrolls.dependencies.MessageFactory') as MessageFactory:
            dependencies = Dependencies().withRequest(sentinel.request)
            dependencies.getMessageFactory()
        MessageFactory.assert_called_with(dependencies, sentinel.request)

    def test_getMessageImporter(self):
        from scrolls.dependencies import Dependencies
        from scrolls.importer import MessageImporter
        dependencies = Dependencies()
        dependency = dependencies.getMessageImporter()
        self.assertIsInstance(dependency, MessageImporter)

    def test_getMessageRepository(self):
        from scrolls.dependencies import Dependencies
        from scrolls.repositories.message import MessageRepository
        dependencies = Dependencies()
        dependency = dependencies.getMessageRepository()
        self.assertIsInstance(dependency, MessageRepository)

    def test_getNginxParser(self):
        from scrolls.dependencies import Dependencies
        from scrolls.parsers.nginx import NginxParser
        dependencies = Dependencies()
        dependency = dependencies.getNginxParser()
        self.assertIsInstance(dependency, NginxParser)

    def test_getRSyslog(self):
        from scrolls.dependencies import Dependencies
        from scrolls.rsyslog import RSyslog
        dependencies = Dependencies()
        dependency = dependencies.getRSyslog()
        self.assertIsInstance(dependency, RSyslog)

    def test_getRSyslogParser(self):
        from scrolls.dependencies import Dependencies
        from scrolls.parsers.rsyslog import RSyslogParser
        dependencies = Dependencies()
        dependency = dependencies.getRSyslogParser()
        self.assertIsInstance(dependency, RSyslogParser)

    def test_getSecurity(self):
        from scrolls.dependencies import Dependencies
        from scrolls.security import Security
        dependencies = Dependencies()
        dependency = dependencies.getSecurity()
        self.assertIsInstance(dependency, Security)

    def test_getServer(self):
        from scrolls.dependencies import Dependencies
        from scrolls.server import Server
        dependencies = Dependencies()
        dependency = dependencies.getServer()
        self.assertIsInstance(dependency, Server)

    def test_getStatisticRepository(self):
        from scrolls.dependencies import Dependencies
        from scrolls.repositories.statistic import StatisticRepository
        dependencies = Dependencies()
        dependency = dependencies.getStatisticRepository()
        self.assertIsInstance(dependency, StatisticRepository)

    def test_getUseragentParser(self):
        from scrolls.dependencies import Dependencies
        from scrolls.parsers.useragent import UseragentParser
        dependencies = Dependencies()
        dependency = dependencies.getUseragentParser()
        self.assertIsInstance(dependency, UseragentParser)

    def test_withRequest(self):
        from scrolls.dependencies import Dependencies
        deps1 = Dependencies()
        request = Mock()
        deps2 = deps1.withRequest(request)
        self.assertNotEqual(deps1, deps2)
