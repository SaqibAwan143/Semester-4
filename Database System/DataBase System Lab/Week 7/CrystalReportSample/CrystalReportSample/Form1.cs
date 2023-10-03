using CrystalDecisions.CrystalReports.Engine;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CrystalReportSample
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            ReportDocument r = new ReportDocument();
            string path = Application.StartupPath;
            string reportpath = @"E:\University\Semester 4\Database System\DataBase System Lab\Week 7\CrystalReportSample\CrystalReportSample\CrystalReport1.rpt";
            string fpath = Path.Combine(path, reportpath);
            r.Load(fpath);
            crystalReportViewer1.ReportSource = r;

        }
    }
}
