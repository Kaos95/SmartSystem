#
# Module to provide access to underlying operating system. Creation of my own os-like
# interface was done to ensure that any underlying os will be configurable (flexible
# architecture).
#
# @author: Hayden McParlane
# @creation-date: 11.12.2015

import abc as _ABC
import configurations as _CONF
from smart_system.system_logging import LoggerFactory as _LOGGER_FACTORY
from smart_system.core.signals import StatusSignal
import unittest as _UNITTEST

###############################################################################
# Module globals
###############################################################################
_L = LoggerFactory.get("core", __name__)

# TODO: Once more is understood about the specific requirements of sensor-based
# operating systems and specifics, this should be refined. Should it be OSInterface
# or hardware interface? What's the appropriate abstraction?

class OSInterface(object):
        '''Abstract base class used for all operating system interfaces.'''
        __metaclass__= _ABC.ABCMeta

	# TODO: Because this is python, apply_configuration is so named and not
	# simply apply(...). This is due to python being dynamically typed.
	# This will be changed when implemented in java and not proof of conce-
	# pt. Cleanliness of code will be greater with that developer interface.
	# Java allows multiple functions with the same name being defined for 
	# diferring parameter definitions. 
        @_ABC.abstractmethod
	def apply_configuration(self, configuration):
		'''Apply the specified configuration on the current host system.
                WARNING: This will apply persistent modifications to the underlying 
                system.'''
		raise NotImplementedError()

	@_ABC.abstractmethod
	def resolve_dependencies(self, dependencies):
		'''Resolve dependencies'''	
		raise NotImplementedError()
		
	@_ABC.abstractmethod
	def resolve_dependency(self, dependency):
		'''Resolve a single dependency.'''
		raise NotImplementedError()

	def setup_environment(...):
	def configure_software(...):
	def start_software(...):
	def verify_software_startup(...):
	def clean_environment(...):

class LinuxInterface(OSInterface):
	import os as _OS
        '''Concrete OSInterface instance for use with linux'''
        def apply_configuration(self, configuration):
		'''Apply a given configuration to the host operating system.'''
		assert(issubclass(configuration, _CONF.Configuration))
		was_success = False

                config = configuration()
                # . Run configuration and installation
		self.resolve_dependencies(config.dependencies)

	def resolve_dependencies(self, dependency_collection):
		'''Resolve the dependencies in the collection.'''
		assert(issubclass(dependency_collection,_CONF.DependencyCollectionInterface))
		was_success = False

		# TODO: In conceptual form --> DependencyCollection isn't actual
		# collection.
		for dependency in dependency_collection:
			self.resolve_dependency(dependency)
		
	def resolve_dependency(self, dependency):	
		'''Resolve the given dependency.'''
		assert(issubclass(dependency, _DEP.DependencyInterface))
		
				

OSInterface.register(LinuxInterface)

class OSType(object):
        '''Abstract base class representing operating system type 
        objects.'''
	__metaclass__ = _ABC.ABCMeta

class LinuxType(OSType):
        '''Object representing linux operating system type.'''
        pass

OSType.register(LinuxType)

class OSInterfaceFactory(object):
        '''Factory used to generate operating system interfaces.'''
        @staticmethod
        def get(os_type):
                '''Returns operating system interface object corresponding to provided
                operating system type.'''
                if not issubclass(os_type.__class__, OSType):
                        raise TypeError("os_type must be a child implementation of "
                                        "OSType.")
                else:
                        # TODO: Make more efficient and refine architecture at this
                        # point.
                        interface = None
                        was_success = False
                        if isinstance(os_type, LinuxType):
                                # TODO: Make more specific than "Linux"
                                interface = LinuxInterface()

                        if interface is not None:
                                was_success = True
                        return StatusSignal(was_success=was_success, payload=interface)

class OSTypeFactory(object):
        '''Factory for generating necessary operating system type objects.'''
        @staticmethod
        def get(os_type_s):
                '''Returns OSType instance.'''
                if os_type_s is None or len(os_type_s) is 0:
			msg = "OSTypeFactory cannot operate on NoneType or "
                                         "an empty string. Value: {}"
                                                .format(os_type_s or "None")
			_L.error(msg)
                        raise ValueError(msg)
                else:
                        os_type_obj = None
                        was_success = False
                        if os_type_s.lowercase() is "linux":
                                os_type_obj = LinuxType()

                        if os_type_obj is not None:
                                was_success = True

                        return StatusSignal(was_success=was_success, payload=os_type_obj)    

################################################################################
# Testing
################################################################################

class LinuxInterfaceTest(_UNITTEST.TestCase):
	def test_to_make_sure_resolve_dependencies_returns_correct_type(self):
		

if __name__ == '__main__':
	#main()
