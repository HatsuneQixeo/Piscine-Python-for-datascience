NAME	:=	ft_package
SRCS	:=	$(shell find . -name "*.py" | grep -v "build/lib/*")
VERSION	:=	1
DIST	:=	dist/${NAME}-${VERSION}-py3-none-any.whl

all: ${DIST}

${DIST}: ${SRCS}
	python3 setup.py sdist bdist_wheel
	pip install $@

clean:
	${RM} -r build dist ${NAME}.egg-info # $$(find . -name "__pycache__")

uninstall: clean
	pip uninstall ${NAME} <<< "Y"

re: uninstall all
