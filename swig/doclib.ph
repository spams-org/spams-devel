#!/usr/bin/perl -w
use strict;
$main::mlab_dir = "../../src_release";

my %undocumented = ("mult",1,"im2col_sliding",1);


%main::conv_names = (
    "Sort", "sort",
    "CalcAAt", "calcAAt",
    "CalcXAt", "calcXAt",
    "CalcXY", "calcXY",
    "CalcXYt", "calcXYt",
    "CalcXtY", "calcXtY",
    "Bayer", "bayer",
    "ConjGrad", "conjGrad",
    "InvSym", "invSym",
    "Normalize", "normalize",
    "SparseProject", "sparseProject",
    "Lasso", "lasso",
    "FistaFlat", "fistaFlat",
    "ProximalFlat", "proximalFlat",
    "TrainDL", "trainDL",
    "TrainDL_Memory", "trainDL_Memory",
    "CD", "cd",
    "LassoMask", "lassoMask",
    "LassoWeighted", "lassoWeighted",
    "OMP", "omp",
    "OMPMask", "ompMask",
    "SOMP", "somp",
    "FistaGraph", "fistaGraph",
    "FistaTree", "fistaTree",
    "ProximalGraph", "proximalGraph",
    "ProximalTree", "proximalTree",
);

%main::tomlab = ();
while( my($k,$v) = each(%main::conv_names)) {
    $main::tomlab{$v} = $k;
}

my $fixed_indent = 4;
%main::alignments = ('Name','NO',
		  'Description' , $fixed_indent,
		  'Usage', 'NO',
		  'Inputs', 'ONKEY',
		  'detail' , $fixed_indent,
		  'Param' , 'ONKEY',
		  'Output' , 'ONKEY',
		  'Author' , 'NO',
		  'WARNING', $fixed_indent,
		  'Note', $fixed_indent,
		  'Examples', $fixed_indent
    );

# in : function name
# out : matlab name (mex...)
sub mlab_name {
    my($name) = @_;
    my $mlab_name = "";
    if(defined($main::tomlab{$name})) {
	$mlab_name = $main::tomlab{$name};
    } else {
	print STDERR "Cannot convert name <$name>\n";
	$mlab_name = $name;
    }
    $mlab_name;
}

# in : matlab name
# out : function name 
sub newname {
    my($mlab_name) = @_;
    my $name = "";
    if(defined($main::conv_names{$mlab_name})) {
	$name = $main::conv_names{$mlab_name};
    } else {
	print STDERR "Cannot convert name <$mlab_name>\n";
	$name = $mlab_name;
    }
    $name;
}
# read .R or .py file containing function definitions
# in : $file = file path
#     $find_func : sub to find the function definition
#     $spams (array) = lines of input file
# out:   $progdefs (hash)  key = progname, val = (i1,i2) indexes of first and last line of a function def
#        $progs (hash)  = function name by function line index
sub read_spams {
    my($file,$find_func,$progdefs,$progs,$spams) = @_;
    open(IN,"<$file") || die "$file open err $!\n";
    my $i = -1;
    my $prog = "";
    my $found = 0;
    my $name = "";
    my $i1 = 0;
    while(<IN>) {
	chomp;
	$i++;
	($prog,$found) = &$find_func("$_",$found);
	if($found) {
	    if("$prog") {
		if(! ($prog =~ /^_/) && ! defined($undocumented{$prog})) {
		    $name = $prog;
		    $i1 = $i;
		} else {$found = 0;}
	    }
	    if($found > 0) {
		$$progdefs{$name} = [($i1,$i)];
		$$progs{$i} = $name;
		$found = 0;
	    }
	}
	push(@$spams,$_);
    }
    close(IN);
}

# read a .m doc file
# in : $f = file path
#      $r_mode (bool) = true if R
#      $mlab_prog = name of matlab function
#      $myprog = name of non matlab function
# out : $doc (hash) = arrays of lines by doc section 
sub get_doc {
    my($f,$r_mode,$mlab_prog,$myprog,$doc) = @_;
    if(! open(IN,"<$f") ) {
	print "ERR $f open err $!\n";
	exit 1;
	return 0;
    }
    my @lines = ();
    my $stat = 0; # 1 when usage is found
    my $prefix = $r_mode ? "spams." : "";
    while(<IN>) {
	chomp;
	s/^%+\s?//;
	if(! $stat) { # skip to Usage
	    (s/^Usage\s*:\s*//) || next;
	    $stat = 1;
	}
	if(/mex([A-Z][_A-z]+)/) { # replace mex*
	    my $s = $1;
	    (defined($main::conv_names{$s}) ) || die "Inconnu : $s\n";
	    my $s1 = $main::conv_names{$s};
	    s/mex$s/$prefix$s1/g;
	}
	push(@lines,$_);
	if(/^Author:/) {last;}
    }
    close(IN);
    ($#lines < 1) && die "No doc in $f!\n";
	
    my $tmp = [()];
    my $deltas = [()]; # indention delta with previous line
    my $key = "";
    my $lang = $r_mode ? "R" : "python";
    $_ = shift(@lines);
    s/^.*=\s*//;
    push(@$tmp,$_);
    $key = 'Usage';
    my $prev_indent = 0;
    foreach $_ (@lines) {
	if(s/^([^\s:]+)\s*:\s*//) { # keys start at the beginning of line
	    my $x = $1;
	    my $i = $#$tmp;
	    # remove last empty lines
	    while($i >= 0) {
		($$tmp[$i] =~ /^\s*$/) || last;
		$i--;
	    }
	    $#$tmp = $i;
	    $#$deltas = $i;
	    $$doc{$key} = {'lines' => $tmp, 'deltas' => $deltas};
	    if(/^\s*$/) {
		$tmp = [()];
		$deltas = [()];
		$prev_indent = 0;
	    } else {
		$tmp = [($_)];
		$deltas = [(0)];
		$prev_indent = set_indent($x);
	    }
	    $key = $x;
	    if ($x eq "Author") {
		$$tmp[0] =~ s/$/ (spams, matlab interface and documentation)/;
		push(@$tmp,"Jean-Paul CHIEZE 2011-2012 ($lang interface)");
#		push(@$tmp,"");
		$deltas = [(0,0)];
		$$doc{$x} = {'lines' => $tmp, 'deltas' => $deltas};
		last;
	    }
	} else {
	    s/^(\s*)//;
	    my $n = length($1);
	    if(/^$/) {$n = $prev_indent;}
	    if(/^param:\s*struct/) {
		$$doc{$key} = {'lines' => $tmp, 'deltas' => $deltas};
		$tmp = [()];
		$deltas = [()];
		$key = "Param";
		next;
	    }
	    if($main::alignments{$key} eq 'NO') {
		$prev_indent = 0;
		$n = 0;
		push(@$deltas,0);
	    } else {
		my $d = $n - $prev_indent;
#		if($d < 0 && $#$deltas == 0) { # realign 1st line of block
#		    $n -= $d;
#		    $d = 0;
#		}
		push(@$deltas,$d);
		$prev_indent = $n;
	    }
	    s/^(\s*)tree:\s*struct\s*/$1tree: named list /;
	    s/param\.lambda([^\w])/param.lambda1$1/;
	    s/(param\.[^\s:]+)\s*:/$1/;
	    if($key eq "Param") {
		if(/^param\.([\w]+)\s*,\s*param\.([\w]+)\s*/) {
		    my $p1 = $1;
		    my $p2 = $2;
		    $n = $$deltas[$#$deltas];
		    push(@$deltas,$n);
		    push(@$tmp,"$p1:");
		    s/^param\.[\w]+\s*,\s*param\.[\w]+\s*/$p2: /;
		} else {
		    if (! /^param\.([^\s]+)\s*=/) {
			s/^param\.([^\s]+)\s/$1: /;
		    }
		}
	    }
	    s/param\.//g;
	    if($r_mode) {
		s/tree\.([A-z_]+)/tree[['$1']]/g;
	    } else {
		s/tree\.([A-z_]+)/tree['$1']/g;
	    }
	    # somme corrections
	    s/group_size/size_group/g;
	    s/Matlab\s+function\s+pcg/$lang function solve/;
	    s/Matlab\s+expression\s+XAt[^\s\;]+/$lang expression/;
	    s/Matlab/$lang/;
#	    if($key eq "Usage") {
##!		s/\s*=\s*/ <- /;
#	    }
	    push(@$tmp,$_);
	}
    }
    close(IN);
    1;
}
sub set_indent {
    my($key) = @_;
    (defined($main::alignments{$key})) || die "No alignment defined for <$key>!\n";
    if ($main::alignments{$key} eq 'NO') {return 0;}
    if($main::alignments{$key} eq 'ONKEY') { return length($key);}
    $main::alignments{$key}; # it must be a nb of spaces
}
sub get_def {
    my ($spams,$progdefs,$myprog,$idt) = @_;
    my $x;
    my @def = ();
    if(! defined($$progdefs{$myprog})) {
	print STDERR "WARNING! No def for <$myprog>\n";
	return ();
    }
    my $ix = $$progdefs{$myprog};
    for(my $i = $$ix[0];$i <= $$ix[1];$i++) {
	$x = $$spams[$i];
	$x =~ s/^\s+//;$x =~ s/\s+$//;
	push(@def,$x);
    }
    $def[0] =~ s/^[^\(]+\(//;
    $def[$#def] =~ s/\)[\s:\{]*$//;
    $x = join('',@def);
    my @tmp = split(/\s*,\s*/,$x);
    my $lgr = $idt;
    $#def = -1;
    my @line = ();
    foreach $x (@tmp) {
	my $n = length($x);
	if(($lgr + $n) > 90) {
	    push(@def,join(",",@line) . ",");
	    @line = ($x);
	    $lgr = $idt + $n + 1;
	} else {
	    push(@line,$x);
	    $lgr += $n + 1;
	}
    }
    if($#line >= 0) {
	push(@def,join(",",@line) . ")");
    } else {
	$def[$#def] =~ s/,$/)/;
    }
    @def;
}

# reads files modifying original doc
# in : $r_mode = true if R
#      $f = data file
# $spams : array of python or R file
# $progdefs (hash)  key = progname, val = (i1,i2) indexes of first and last line of a function def
# special replacement of %DEF% in Usage section
# 
# out : $modifs (hash) = modifications by doc section
sub get_modifs {
    my($r_mode,$f,$myprog,$modifs,$spams,$progdefs) = @_;
    my @lines = ();
    open(IN,"<$f") || return;
    while(<IN>) {
	chomp;
	if(s/^include\s+//) {
	    my $f2 = $_;
	    my $d = $f;
	    $d =~ s:[^/]+$::;
	    if(open(INC,"<$d$f2")) {
		while(<INC>) {
		    chomp;
		    push(@lines,$_);
		}
		close(INC);
	    }
	    next;
	}
	push(@lines,$_);
    }
    close(IN);
    my $inblock = 0;
    my ($tmp,$key,,$deltas,$op,$prev_indent);
    my $expr = "";
    foreach $_ (@lines) {
	(/^\s*$/) && next;
	(/^\s*\#/) && next;
	if(s/^\[([PR])\]//) {  # this line is only for R or python
	    my $x = ($1 eq "P") ? 0 : 1;
	    ($x == $r_mode) || next;
	}
	if(! $r_mode) { s/<-/=/;}
	if($inblock) {
	    if(/^end/) {
		$inblock = 0;
		$$modifs{$key} = { 'op' => $op, 'lines' => $tmp, 'deltas' => $deltas};
		if("$expr") {
		    my $x = $$modifs{$key};
		    $$x{'subst'} = $expr;
		    $expr = "";
		}
		next;
	    }
	    if($key eq 'Usage' && ! $r_mode) {
		s/<-/=/;
	    }
	    if(/%DEF%/) {
		my $name = $r_mode ? "spams.$myprog" : $myprog;
		s/%DEF%.*$/spams.$myprog\(/;
		my $n = length($_);
		my $idt = " " x $n;
		my @def = get_def($spams,$progdefs,$myprog,$n);
		$_ .= shift(@def);
		push(@$tmp,$_);
		push(@$deltas,0);
		foreach $_ (@def) {
		    push(@$tmp,"$idt$_");
		    push(@$deltas,0);
		}
	    } else {
		my $d = 0;
		s/^(\s*)//;
		my $n = length($1);
		if(! (/^$/)) {
		    $d = $n - $prev_indent;
		    if($d < 0 && $#$tmp < 0) {
			$d = 0;
		    }
		    $prev_indent = $n;
		    if($key eq "Param" && ($_ =~ /:\s*$/)) {
			s/$/    undocumented; modify at your own risks!/;
		    }
		}
		push(@$tmp,$_);
		push(@$deltas,$d);
	    }
	} else {
	    (/^begin\s+([^\s]+)\s+([^\s]+)$/) || next;
	    $op = $1;
	    $key = $2;
	    $tmp = [()];
	    $deltas = [()];
	    $inblock = 1;
	    $prev_indent = set_indent($key);
	}
    }
}

# try to split Description into short description and detail
sub split_description {
    my($doc) = @_;
    my $l = $$doc{'Description'};
    my $tmp = $$l{'lines'};
    my $deltas = $$l{'deltas'};
    my $det = [()];
    my $dltdet = [()];
    ($#$tmp < 3) && return;
    for(my $i = 0;$i <= $#$tmp;$i++) {
	my $s = $$tmp[$i];
	if(($s =~ /^$/) || ($s =~ /\.$/)) {
	    my $j = $i;
	    $i++;
	    while($i <= $#$tmp) {
		push(@$dltdet,$$deltas[$i]);
		push(@$det,$$tmp[$i++]);
	    }
	    $$doc{'detail'} = {'lines' => $det, 'deltas' => $dltdet};
	    $#$tmp = $j;
	    $#$deltas = $j;
	    last;
	}
		
    }
}
# modify $doc according to $modifs
# 
sub apply_modifs {
    my($doc,$format,$modifs) = @_;
    my($op,$tmp,$deltas);
    while(my ($key,$x) = each(%$modifs)) {
	if(! defined($$format{$key})) {
	    print "Warning: Unknown modif key <$key>\n";
	    next;
	}
	$op = $$x{'op'};
	$tmp = $$x{'lines'};
	$deltas = $$x{'deltas'};
	if($op eq "repl") {
	    $$doc{$key} = {'lines' => $tmp, 'deltas' => $deltas};
	
	} else {
	    (defined($$format{$key})) || next;
	    my ($lst,$ddeltas) = ([()], [()]);
	    if(defined($$doc{$key})) {
		my $l = $$doc{$key};
		$lst = $$l{'lines'};
		$ddeltas = $$l{'deltas'}
	    }
	    if ( $op eq "addfirst") {
		die "Addfirst not implemented\n";
	    } elsif ( $op eq "addlast") {
		push(@$lst,@$tmp);
		push(@$ddeltas,@$deltas);
		$$doc{$key} = {'lines' => $lst, 'deltas' => $ddeltas};
	    } elsif ( $op eq "subst") {
		my $e = $$tmp[0];
		$e =~ s/^\s+//;
		for(my$i = 0;$i <= $#$lst;$i++) {
		    my $s = $$lst[$i];
		    eval("\$s =~ $e");
		    $$lst[$i] = $s;
		}
	    } else {
		die "Unknown op $op\n";
	    }
	}
    }
}

# IN: $r_mode = 0/1 for python/R
# $mlab_prog = prog name in matlab
# $myprog = prog name for python or R
# $doc : empty doc hash table
# $format : hash table describing format of the different parts of doc
# $spams : array of python or R file
# $progdefs (hash)  key = progname, val = (i1,i2) indexes of first and last line of a function def
# Out : $doc of the function
sub prepare_doc {
    my($r_mode,$mlab_prog,$myprog,$doc,$format,$spams,$progdefs) = @_;
    my $f = "$main::mlab_dir/mex$mlab_prog.m";
    my $fref = "./refman/$myprog.in";
    my %modifs = ();
    get_doc($f,$r_mode,$mlab_prog,$myprog,$doc) || return;
    split_description($doc);

    get_modifs($r_mode,$fref,$myprog,\%modifs,$spams,$progdefs);
    # apply modifs
    apply_modifs($doc,$format,\%modifs);
}

############## latex output ###############
@main::texkeys = ('Name','Usage','Description','Inputs', 'Output','Author','Note','Examples');

$main::tex_docformat = {
    'Name' => {'no_nl' => 1},
    'Description' => {},
    'Usage' => {'no_nl' => 1},
    'Inputs' => {},
    'Param' => {},
    'detail' => {},
    'Output' => {'indent' => 1},
    'Author' => {'tag' => 'Authors'},
    'Note' => {'tag' => 'Note', 'optional' => 1},
    'Examples' => {'tag' => 'Examples', 'optional' => 1},
};

# in : $indx : array of last line of function def
sub make_tex_doc {
    my($r_mode,$dir,$indx,$progs,$spams,$progdefs) = @_;
    foreach my $i (@$indx) {
	my $myprog = $$progs{$i};
##	($myprog eq "trainDL") || next;
	my $mlab_prog = mlab_name($myprog);
	my %doc = ();
	prepare_doc($r_mode,$mlab_prog,$myprog,\%doc,$main::tex_docformat,$spams,$progdefs);
	print "++ $myprog\n";
	write_tex_man("$dir/functions/$myprog.in",$myprog,\%doc,$main::tex_docformat);
    }
    modif_tex_src($r_mode,$dir);
}
sub xindent_lines {
    my($lines,$deltas,$i0,$indent0) = @_;
    my @res = ();
    my $nindent = $indent0;
    # adjust
    my $adj = 0;
    my $pos = $nindent;
    for (my $i = $i0; $i <= $#$lines;$i++) {
	my $n = $$deltas[$i];
	$pos += $n;
	if($pos < $adj) {$adj = $pos;}
    }
    $nindent -= $adj;
    for (my $i = $i0; $i <= $#$lines;$i++) {
	my $s = $$lines[$i];
	my $n = $$deltas[$i];
	$nindent += $n;
	if($nindent < 0) {print "Indent < 0, $i <$s>, $n\n";}
	if($nindent > 0) {
	    my $sp = " " x $nindent;
	    $s = "$sp$s";
	}
	push(@res,$s);
    }
    @res;
}
sub indent_lines {
    my($lines,$deltas,$key) = @_;
    my @res = ();
    my $indent0 = set_indent($key);
    my $nindent = $indent0;
    # adjust
    for (my $i = 0; $i <= $#$lines;$i++) {
	my $s = $$lines[$i];
	my $n = $$deltas[$i];
	$nindent += $n;
	if(($main::alignments{$key} eq "ONKEY") && ($s =~ /^[^\s:]+\s*:/)) { #reset alignment
	    $nindent = $indent0;
	}
	if($nindent < 0) {print "Indent < 0, $i <$s>, $n\n";}
	if($nindent > 0) {
	    my $sp = " " x $nindent;
	    $s = "$sp$s";
	}
	push(@res,$s);
    }
    @res;
}

sub merge_doc {
    my($doc,$tagin,$tagout) = @_;

    if(defined($$doc{$tagin})) {
	my $lin = $$doc{$tagin};
	my $lout = $$doc{$tagout};
	my $doco = $$lout{'lines'};
	my $dlto = $$lout{'deltas'};
	my $doci = $$lin{'lines'};
	my $dlti = $$lin{'deltas'};
	push(@$doco,@$doci);
	push(@$dlto,@$dlti);
	undef($$doc{$tagin});
    }
}  
sub write_tex_man {
    my ($f,$prog,$doc,$rdformat) = @_;
    my($rdf,$i,$key,$tmp,$deltas);
    merge_doc($doc,'Param','Inputs');
    merge_doc($doc,'detail','Description');
    open(OUT,">$f") || die "$f create err $!\n";
    print OUT "#\n";
    foreach $key (@main::texkeys) {
	(defined($$rdformat{$key})) || next;
	$rdf = $$rdformat{$key};
	if(! defined($$doc{$key})) {
	    if(! defined($$rdf{'optional'})) {
		print STDERR "!! $prog : $key MISSING.\n";
	    }
	    next;
	}
	my $l = $$doc{$key};
	$tmp = $$l{'lines'};
	$deltas = $$l{'deltas'};
	my $tag = (defined($$rdf{'tag'})) ? $$rdf{'tag'} : $key;
	if(defined($$rdf{'no_nl'})) {
	    print OUT "# $tag: ";
	} else {
	    print OUT "# $tag:\n# ";
	}
	if(defined($$rdf{'prog'})) {
	    my $func = $$rdf{'prog'};
	    my @res = &$func($tmp);
	    print OUT join("\n",@res), "\n}\n";
	} else {
	    my @res = indent_lines($tmp,$deltas,$key);
	    print OUT join("\n# ",@res), "\n#\n";
	}
    }
    
    close(OUT);
}

sub insert_install {
    my($fh) = @_;
    open(INST,"<install.tex") || die "install.tex open err $!\n";
    while(<INST>) {
	print $fh $_;
    }
    close(INST)
}

sub modif_tex_src {
    my ($r_mode,$dir) = @_;
    open(IN,"<../../doc/doc_spams.tex") || die "Cannot read ../../doc/doc_spams.tex: $!\n";
    open(OUT,">$dir/doc_spams.tex") || die "Cannot create $dir/doc_spams.tex\n";
    my $in_install = 0;
    while(<IN>) {
	chomp;
	if(/^\\section\{Installation/) {
	    $in_install = 1;
	    print OUT "\\section{Installation}\n";
	    insert_install(\*OUT);
	    next;
	}
	if($in_install) {
	    if(/^\\section\{/) {
		$in_install = 0;
	    } else {next;}
	}
	if(/mex([A-Z][_A-z]+)/) {
	    my $s = $1;
	    my $x = $s;
	    $x =~ s/\\_/_/;
	    $s =~ s/\\/\\\\/;
	    if (! defined($main::conv_names{$x}) ) {
		print STDERR "Unkown $s\n";
	    } else {
		my $s1 = $main::conv_names{$x};
		$x = $s1;
		$s1 =~ s/_/\\_/;
		s/mex$s/spams.$s1/g;
	    }
	    if(/verbatiminput/) {
	      s|../src_release/spams\.(.*)\.m|functions/$1.in|;
	      s/\\_/_/;
	      if (! -r "$dir/functions/$x.in") {
		  $_ = "\\verbatiminput{functions/missing.in}";
	      }
	    }
	}
	print OUT "$_\n";
    }
    close(IN);
    close(OUT);
}
1;
