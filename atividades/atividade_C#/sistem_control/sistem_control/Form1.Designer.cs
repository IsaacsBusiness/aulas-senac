namespace sistem_control
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            pictureBox1 = new PictureBox();
            label1 = new Label();
            button1 = new Button();
            lblLogin = new Label();
            txtSenha = new TextBox();
            lblSenha = new Label();
            txtLogin = new TextBox();
            tableLayoutPanel1 = new TableLayoutPanel();
            checkBox1 = new CheckBox();
            linkLabel1 = new LinkLabel();
            pictureBox2 = new PictureBox();
            ((System.ComponentModel.ISupportInitialize)pictureBox1).BeginInit();
            tableLayoutPanel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)pictureBox2).BeginInit();
            SuspendLayout();
            // 
            // pictureBox1
            // 
            pictureBox1.Anchor = AnchorStyles.None;
            pictureBox1.BackColor = Color.Transparent;
            pictureBox1.Image = Properties.Resources.a2e5f86a_6255_4836_b898_486021542a62;
            pictureBox1.Location = new Point(304, 28);
            pictureBox1.Name = "pictureBox1";
            pictureBox1.Size = new Size(205, 166);
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.TabIndex = 1;
            pictureBox1.TabStop = false;
            // 
            // label1
            // 
            label1.Anchor = AnchorStyles.None;
            label1.AutoSize = true;
            label1.BackColor = Color.FromArgb(163, 163, 113);
            label1.Font = new Font("Segoe UI", 15F, FontStyle.Bold);
            label1.Location = new Point(322, 219);
            label1.Name = "label1";
            label1.Size = new Size(187, 28);
            label1.TabIndex = 5;
            label1.Text = "Gestão de Estoque";
            label1.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // button1
            // 
            button1.Anchor = AnchorStyles.None;
            button1.BackColor = Color.White;
            button1.Cursor = Cursors.Hand;
            button1.FlatAppearance.BorderColor = Color.White;
            button1.FlatAppearance.BorderSize = 0;
            button1.FlatAppearance.MouseDownBackColor = Color.Violet;
            button1.FlatAppearance.MouseOverBackColor = Color.FromArgb(76, 91, 55);
            button1.FlatStyle = FlatStyle.Flat;
            button1.Font = new Font("Segoe UI", 12F, FontStyle.Bold);
            button1.ForeColor = Color.Black;
            button1.Location = new Point(349, 389);
            button1.Name = "button1";
            button1.Size = new Size(131, 39);
            button1.TabIndex = 6;
            button1.Text = "Entrar";
            button1.UseVisualStyleBackColor = false;
            // 
            // lblLogin
            // 
            lblLogin.Anchor = AnchorStyles.Left;
            lblLogin.Font = new Font("Segoe UI", 10F, FontStyle.Bold);
            lblLogin.Location = new Point(3, 8);
            lblLogin.Name = "lblLogin";
            lblLogin.Size = new Size(64, 19);
            lblLogin.TabIndex = 2;
            lblLogin.Text = "Usuário:";
            lblLogin.Click += lblLogin_Click;
            // 
            // txtSenha
            // 
            txtSenha.Anchor = AnchorStyles.None;
            txtSenha.Location = new Point(93, 42);
            txtSenha.Name = "txtSenha";
            txtSenha.Size = new Size(148, 25);
            txtSenha.TabIndex = 4;
            // 
            // lblSenha
            // 
            lblSenha.Anchor = AnchorStyles.Left;
            lblSenha.AutoSize = true;
            lblSenha.Font = new Font("Segoe UI", 10F, FontStyle.Bold);
            lblSenha.Location = new Point(3, 45);
            lblSenha.Name = "lblSenha";
            lblSenha.Size = new Size(53, 19);
            lblSenha.TabIndex = 3;
            lblSenha.Text = "Senha:";
            lblSenha.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // txtLogin
            // 
            txtLogin.Anchor = AnchorStyles.None;
            txtLogin.Location = new Point(93, 5);
            txtLogin.Name = "txtLogin";
            txtLogin.Size = new Size(147, 25);
            txtLogin.TabIndex = 0;
            // 
            // tableLayoutPanel1
            // 
            tableLayoutPanel1.Anchor = AnchorStyles.None;
            tableLayoutPanel1.BackColor = Color.FromArgb(163, 163, 113);
            tableLayoutPanel1.ColumnCount = 2;
            tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle());
            tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 73.5119F));
            tableLayoutPanel1.Controls.Add(lblSenha, 0, 1);
            tableLayoutPanel1.Controls.Add(lblLogin, 0, 0);
            tableLayoutPanel1.Controls.Add(txtSenha, 1, 1);
            tableLayoutPanel1.Controls.Add(txtLogin, 1, 0);
            tableLayoutPanel1.GrowStyle = TableLayoutPanelGrowStyle.AddColumns;
            tableLayoutPanel1.Location = new Point(290, 270);
            tableLayoutPanel1.Name = "tableLayoutPanel1";
            tableLayoutPanel1.RowCount = 2;
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
            tableLayoutPanel1.Size = new Size(264, 73);
            tableLayoutPanel1.TabIndex = 7;
            tableLayoutPanel1.Paint += tableLayoutPanel1_Paint;
            // 
            // checkBox1
            // 
            checkBox1.Anchor = AnchorStyles.None;
            checkBox1.AutoSize = true;
            checkBox1.BackColor = Color.FromArgb(163, 163, 113);
            checkBox1.Location = new Point(300, 345);
            checkBox1.Name = "checkBox1";
            checkBox1.Size = new Size(130, 23);
            checkBox1.TabIndex = 8;
            checkBox1.Text = "Lembrar Usuário";
            checkBox1.UseVisualStyleBackColor = false;
            checkBox1.CheckedChanged += checkBox1_CheckedChanged;
            // 
            // linkLabel1
            // 
            linkLabel1.Anchor = AnchorStyles.None;
            linkLabel1.AutoSize = true;
            linkLabel1.BackColor = Color.FromArgb(163, 163, 113);
            linkLabel1.LinkColor = Color.RoyalBlue;
            linkLabel1.Location = new Point(436, 345);
            linkLabel1.Name = "linkLabel1";
            linkLabel1.Size = new Size(95, 19);
            linkLabel1.TabIndex = 9;
            linkLabel1.TabStop = true;
            linkLabel1.Text = "Esqueci Senha";
            linkLabel1.LinkClicked += linkLabel1_LinkClicked;
            // 
            // pictureBox2
            // 
            pictureBox2.Anchor = AnchorStyles.None;
            pictureBox2.BackColor = Color.FromArgb(163, 163, 113);
            pictureBox2.BackgroundImageLayout = ImageLayout.Zoom;
            pictureBox2.Location = new Point(274, 200);
            pictureBox2.Name = "pictureBox2";
            pictureBox2.Size = new Size(280, 248);
            pictureBox2.TabIndex = 10;
            pictureBox2.TabStop = false;
            // 
            // Form1
            // 
            AutoScaleMode = AutoScaleMode.Inherit;
            AutoSizeMode = AutoSizeMode.GrowAndShrink;
            BackColor = Color.FromArgb(76, 91, 55);
            ClientSize = new Size(800, 487);
            Controls.Add(linkLabel1);
            Controls.Add(checkBox1);
            Controls.Add(tableLayoutPanel1);
            Controls.Add(label1);
            Controls.Add(pictureBox1);
            Controls.Add(button1);
            Controls.Add(pictureBox2);
            Font = new Font("Segoe UI", 10F);
            Name = "Form1";
            StartPosition = FormStartPosition.CenterScreen;
            Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)pictureBox1).EndInit();
            tableLayoutPanel1.ResumeLayout(false);
            tableLayoutPanel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)pictureBox2).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion
        private PictureBox pictureBox1;
        private Label label1;
        private Button button1;
        private Label lblLogin;
        private TextBox txtSenha;
        private Label lblSenha;
        private TextBox txtLogin;
        private TableLayoutPanel tableLayoutPanel1;
        private CheckBox checkBox1;
        private LinkLabel linkLabel1;
        private PictureBox pictureBox2;
    }
}
