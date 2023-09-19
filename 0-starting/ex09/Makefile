NAME	:=	ft_package
SRCS	:=	$(shell find . -name "*.py" | grep -v "build/lib/*")
VERSION	:=	0.0.1
DIST	:=	dist/${NAME}-${VERSION}-py3-none-any.whl

all: ${DIST}

${DIST}: ${SRCS}
	python3 setup.py sdist bdist_wheel
	${MAKE} install

install: ${DIST}
	pip install $<

clean:
	${RM} -r build dist ${NAME}.egg-info # $$(find . -name "__pycache__")

uninstall: clean
	pip uninstall ${NAME} <<< "Y"

re: uninstall all
