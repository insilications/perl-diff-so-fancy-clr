message(STATUS "cmake version ${CMAKE_VERSION}")
project(perl-diff-so-fancy)
cmake_minimum_required (VERSION 2.8.8) # OBJECT libraries require 2.8.8

set(PERL_BIN_LIB_INSTALL_DIR /usr/bin/lib/ CACHE STRING "PERL_BIN_LIB_INSTALL_DIR install location")

install(PROGRAMS ${PROJECT_SOURCE_DIR}/diff-so-fancy TYPE BIN)
install(FILES ${PROJECT_SOURCE_DIR}/lib/DiffHighlight.pm DESTINATION ${PERL_BIN_LIB_INSTALL_DIR})
