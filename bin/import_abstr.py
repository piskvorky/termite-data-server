#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

APPS_ROOT = 'apps'
WEB2PY_ROOT = 'web2py'
SUBFOLDERS = [ 'models', 'views', 'controllers', 'static', 'modules' ]

class ImportAbstraction( object ):
	
	def __init__( self, app_name, app_model, app_desc ):
		self.app_path = '{}/{}'.format( APPS_ROOT, app_name )
		self.data_path = '{}/{}/data/{}'.format( APPS_ROOT, app_name, app_model )
		self.web2py_path = '{}/applications/{}'.format( WEB2PY_ROOT, app_name )
		
		self.database_path = '{}/{}/databases'.format( APPS_ROOT, app_name )
		
		print '--------------------------------------------------------------------------------'
		print 'Import "{}" as a web2py application...'.format( app_desc )
		print '          app = {}'.format( app_name )
		print '        model = {}'.format( app_model )
		print '     app_path = {}'.format( self.app_path )
		print '    data_path = {}'.format( self.data_path )
		print 'database_path = {}'.format( self.database_path )
		print '  web2py_path = {}'.format( self.web2py_path )
		print '--------------------------------------------------------------------------------'
		
		if not os.path.exists( self.app_path ):
			print 'Creating app folder: {}'.format( self.app_path )
			os.makedirs( self.app_path )
		
		if not os.path.exists( self.data_path ):
			print 'Creating data subfolder: {}'.format( self.data_path )
			os.makedirs( self.data_path )
		
		if not os.path.exists( self.database_path ):
			print 'Creating database subfolder: {}'.format( self.database_path )
			os.makedirs( self.database_path )
		
		for subfolder in SUBFOLDERS:
			app_subpath = '{}/{}'.format( self.app_path, subfolder )
			if not os.path.exists( app_subpath ):
				print 'Linking subfolder: {}'.format( app_subpath )
				os.system( 'ln -s ../../server_src/{} {}/{}'.format( subfolder, self.app_path, subfolder ) )
		
		filename = '{}/__init__.py'.format( self.app_path )
		if not os.path.exists( filename ):
			print 'Setting up __init__.py'
			os.system( 'touch {}'.format( filename ) )
	
	def AddToWeb2py( self ):
		if not os.path.exists( self.web2py_path ):
			print 'Adding app to web2py server: {}'.format( self.web2py_path )
			os.system( 'ln -s ../../{} {}'.format( self.app_path, self.web2py_path ) )
		print '--------------------------------------------------------------------------------'
