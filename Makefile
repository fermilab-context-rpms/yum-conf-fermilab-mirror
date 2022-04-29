_default:
	@echo "make"
sources:
	@echo "make sources"
	@tar cvf - repos | gzip --best > yum-conf-fermilab-mirror-sources.tar.gz
srpm: sources
	rpmbuild -bs --define '_sourcedir .' --define '_srcrpmdir .' yum-conf-fermilab-mirror.spec
