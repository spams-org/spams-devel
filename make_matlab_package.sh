rm -rf spams-matlab
svn export branches/v2.2 spams-matlab
rm -rf spams-matlab/swig/
rm spams/make_matlab_package.sh
da=$(``date +%F)
echo $da
tar -czf spams-matlab-v2.2-svn$da.tar.gz spams-matlab
rm -rf spams-matlab

