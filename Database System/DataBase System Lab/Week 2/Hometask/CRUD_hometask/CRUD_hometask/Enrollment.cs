using CRUD_Operations;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.Common;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace CRUD_hometask
{
    public partial class Enrollment : Form
    {
        public Enrollment()
        {
            InitializeComponent();
        }

        private void Enrollment_Load(object sender, EventArgs e)
        {
            var con = Configuration.getInstance().getConnection();
            
                
            try
            {
                SqlDataReader myReader1 = null;
                SqlCommand myCommand1 = new SqlCommand("select Course_Name from Courses", con);
                myReader1 = myCommand1.ExecuteReader();
                while (myReader1.Read())
                {
                    comboBox2.Items.Add((string)myReader1["Course_Name"]);
                }
                myReader1.Close();
            }
            catch
            {

            }

            SqlDataReader myReader = null;

            SqlCommand myCommand = new SqlCommand("select RegNumber from StuRecord", con);

            myReader = myCommand.ExecuteReader();

            while (myReader.Read())
            {
                comboBox1.Items.Add((string)myReader["RegNumber"]);
            }
            myReader.Close();

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (comboBox1.Text != "" && comboBox2.Text != "" )
            {
                var con = Configuration.getInstance().getConnection();
                SqlCommand cmd = new SqlCommand("insert into Enrollment values(@StudentRegNo,@CourseName)", con);
                cmd.Parameters.AddWithValue("@StudentRegNo", comboBox1.Text);
                cmd.Parameters.AddWithValue("@CourseName", comboBox2.Text);
                cmd.ExecuteNonQuery();
                MessageBox.Show("Student Enrolled Successfully");
                
            }
            else
            {
                MessageBox.Show("Please Provide Details!");
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (comboBox1.Text != "" && comboBox2.Text != "")
            {
                var con = Configuration.getInstance().getConnection();
                SqlCommand cmd = new SqlCommand("delete Enrollment where StudentRegNo=@StudentRegNo and CourseName=@CourseName", con);
                cmd.Parameters.AddWithValue("@StudentRegNo", comboBox1.Text);
                cmd.Parameters.AddWithValue("@CourseName", comboBox2.Text);
                cmd.ExecuteNonQuery();
                MessageBox.Show("Unregistered Successfully!");

            }
            else
            {
                MessageBox.Show("Please Select Enrolled Student to Delete");
            }
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            var con = Configuration.getInstance().getConnection();
            SqlCommand cmd = new SqlCommand("Select * from Enrollment", con);
            SqlDataAdapter da = new SqlDataAdapter(cmd);
            DataTable dt = new DataTable();
            da.Fill(dt);
            dataGridView1.DataSource = dt;
        }
    }
}
