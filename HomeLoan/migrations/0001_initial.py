# Generated by Django 4.0.3 on 2022-09-18 13:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('bank_id', models.AutoField(primary_key=True, serialize=False)),
                ('bank_name', models.CharField(max_length=25)),
                ('cust_type', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='CostSheet',
            fields=[
                ('cost_particular_id', models.AutoField(primary_key=True, serialize=False)),
                ('particulars', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='HlBasicDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationality', models.CharField(max_length=50)),
                ('minimum_age', models.IntegerField()),
                ('retirement_age', models.IntegerField()),
                ('maximum_age_consider_govt', models.IntegerField()),
                ('maximum_age_consider_others', models.IntegerField()),
                ('minimum_loan_amount', models.FloatField()),
                ('maximum_loan_amount', models.FloatField()),
                ('total_experience', models.IntegerField()),
                ('company_profitability', models.BooleanField()),
                ('form_16', models.BooleanField()),
                ('profession_tax_deduction', models.BooleanField()),
                ('negative_employer_profile', models.BooleanField()),
                ('effective_date', models.DateTimeField(blank=True, null=True)),
                ('ineffective_date', models.DateTimeField(blank=True, null=True)),
                ('company_type', models.ManyToManyField(to='master.companytype')),
                ('customer_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.customertype')),
                ('designation', models.ManyToManyField(to='master.designationtype')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsAndPolicy',
            fields=[
                ('prod_id', models.AutoField(primary_key=True, serialize=False)),
                ('productandpolicy_name', models.CharField(max_length=50, unique=True)),
                ('effective_date', models.DateField(blank=True, null=True)),
                ('ineffective_date', models.DateField(blank=True, null=True)),
                ('lock', models.BooleanField(default=False)),
                ('bank_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.bankname')),
                ('prod_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.product')),
                ('sub_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.subproduct')),
            ],
        ),
        migrations.CreateModel(
            name='Remarks',
            fields=[
                ('remark_id', models.AutoField(primary_key=True, serialize=False)),
                ('remark', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('prop_id', models.AutoField(primary_key=True, serialize=False)),
                ('builder_cat', models.CharField(max_length=25)),
                ('occupation_certi', models.CharField(max_length=25)),
                ('prev_agreement', models.CharField(max_length=25)),
                ('sub_scheme', models.CharField(max_length=25)),
                ('perc_completion', models.IntegerField()),
                ('bank_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.bank')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.productsandpolicy')),
            ],
        ),
        migrations.CreateModel(
            name='OtherDetailsROI',
            fields=[
                ('oth_det_roi_id', models.AutoField(primary_key=True, serialize=False)),
                ('min_loan_amt', models.IntegerField()),
                ('max_loan_amt', models.IntegerField()),
                ('min_val', models.IntegerField()),
                ('max_val', models.IntegerField()),
                ('roi_women', models.CharField(max_length=5)),
                ('roi_men', models.CharField(max_length=5)),
                ('bank_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.bank')),
            ],
        ),
        migrations.CreateModel(
            name='OtherDetails',
            fields=[
                ('oth_det_id', models.AutoField(primary_key=True, serialize=False)),
                ('prevailing_rate', models.IntegerField()),
                ('tenure', models.CharField(max_length=25)),
                ('inward_cheque_return', models.CharField(max_length=25)),
                ('multiple_inquiry', models.CharField(max_length=25)),
                ('bank_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.bank')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.productsandpolicy')),
            ],
        ),
        migrations.CreateModel(
            name='Obligation',
            fields=[
                ('obligation_id', models.AutoField(primary_key=True, serialize=False)),
                ('emi_oblig', models.CharField(max_length=25)),
                ('emi_oblig_not_consi', models.CharField(max_length=25)),
                ('credit_card', models.CharField(max_length=25)),
                ('credit_card_oblig_percent', models.IntegerField()),
                ('gold_loan', models.CharField(max_length=25)),
                ('gold_loan_percent', models.IntegerField()),
                ('bank_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.bank')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.productsandpolicy')),
            ],
        ),
        migrations.CreateModel(
            name='NegativeEmployerProfile',
            fields=[
                ('neg_emp_pro_id', models.AutoField(primary_key=True, serialize=False)),
                ('neg_emp_pro', models.CharField(max_length=25)),
                ('bank_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.bank')),
            ],
        ),
        migrations.CreateModel(
            name='LtvResale',
            fields=[
                ('ltv_id', models.AutoField(primary_key=True, serialize=False)),
                ('min_amount', models.IntegerField()),
                ('max_amount', models.IntegerField()),
                ('rbi_guidelines', models.IntegerField()),
                ('doccument_cost', models.IntegerField()),
                ('additional', models.IntegerField()),
                ('car_parking', models.IntegerField()),
                ('total', models.IntegerField()),
                ('market_value', models.IntegerField()),
                ('av_capping', models.IntegerField()),
                ('bank_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.bank')),
            ],
        ),
        migrations.CreateModel(
            name='LoanTowardsValuation',
            fields=[
                ('loan_tow_val_id', models.AutoField(primary_key=True, serialize=False)),
                ('cost_sheet', models.CharField(max_length=90)),
                ('min_amount', models.IntegerField()),
                ('max_amount', models.IntegerField()),
                ('rbi_guidelines', models.CharField(max_length=25)),
                ('ammenity', models.CharField(max_length=25)),
                ('additional', models.CharField(max_length=25)),
                ('car_parking', models.CharField(max_length=25)),
                ('car_parking_percent', models.CharField(max_length=25)),
                ('bank_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.bank')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.productsandpolicy')),
            ],
        ),
        migrations.CreateModel(
            name='IncomeFoir',
            fields=[
                ('inc_foir_id', models.AutoField(primary_key=True, serialize=False)),
                ('min_amt', models.IntegerField()),
                ('max_amt', models.IntegerField()),
                ('percent', models.IntegerField()),
                ('bank_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.bank')),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('income_id', models.AutoField(primary_key=True, serialize=False)),
                ('gross_sal', models.CharField(max_length=25)),
                ('net_sal', models.CharField(max_length=25)),
                ('bonus', models.CharField(max_length=25)),
                ('bonus_avg_yearly', models.CharField(max_length=25)),
                ('bonus_avg_yearly_percent', models.CharField(max_length=25)),
                ('bonus_avg_qtr', models.CharField(max_length=25)),
                ('bonus_avg_qtr_percent', models.CharField(max_length=25)),
                ('bonus_avg_half_yearly', models.CharField(max_length=25)),
                ('bonus_avg_half_yearly_percent', models.CharField(max_length=25)),
                ('rent_income', models.CharField(max_length=25)),
                ('rent_agreement_type', models.CharField(max_length=25)),
                ('bank_ref', models.CharField(max_length=25)),
                ('rent_ref_in_bank', models.CharField(max_length=25)),
                ('rent_inc_percent', models.CharField(max_length=25)),
                ('fut_rent', models.CharField(max_length=25)),
                ('fut_rent_percent', models.CharField(max_length=25)),
                ('incentive', models.CharField(max_length=25)),
                ('incen_avg_months', models.CharField(max_length=25)),
                ('incen_percent', models.CharField(max_length=25)),
                ('coApplicant_No_Income_only_Rent_income', models.CharField(max_length=25)),
                ('bank_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.bank')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.productsandpolicy')),
            ],
        ),
        migrations.CreateModel(
            name='HlProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('builder_category', models.BooleanField()),
                ('apf', models.BooleanField()),
                ('occupation_certificate', models.BooleanField()),
                ('cc_municipal_plan_tax_receipt', models.BooleanField()),
                ('previous_aggrement_available', models.BooleanField()),
                ('subvention_scheme', models.BooleanField()),
                ('percent_of_completion', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('property_age', models.IntegerField(blank=True, null=True)),
                ('effective_date', models.DateTimeField(blank=True, null=True)),
                ('ineffective_date', models.DateTimeField(blank=True, null=True)),
                ('basic_details_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.hlbasicdetails')),
                ('negative_area', models.ManyToManyField(to='master.negativearea')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.productsandpolicy')),
                ('property_type', models.ManyToManyField(to='master.propertytype')),
                ('room_type', models.ManyToManyField(to='master.roomtype')),
                ('stage_of_construction', models.ManyToManyField(to='master.stageofconstruction')),
            ],
        ),
        migrations.CreateModel(
            name='HlOtherDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_of_interest', models.IntegerField()),
                ('prevailing_rate', models.IntegerField()),
                ('tenure', models.IntegerField()),
                ('inward_cheque_return', models.BooleanField()),
                ('multiple_inquiry', models.BooleanField()),
                ('relation_eligible', models.CharField(max_length=25)),
                ('relation_not_eligible', models.CharField(max_length=25)),
                ('effective_date', models.DateTimeField(blank=True, null=True)),
                ('ineffective_date', models.DateTimeField(blank=True, null=True)),
                ('basic_details_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.hlbasicdetails')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.productsandpolicy')),
            ],
        ),
        migrations.CreateModel(
            name='HlObligation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emi_obligation', models.BooleanField()),
                ('emi_obligation_not_consider', models.IntegerField()),
                ('credit_card', models.BooleanField()),
                ('credit_card_obligation_percent', models.IntegerField()),
                ('gold_loan', models.BooleanField()),
                ('gold_loan_percent', models.IntegerField()),
                ('effective_date', models.DateTimeField(blank=True, null=True)),
                ('ineffective_date', models.DateTimeField(blank=True, null=True)),
                ('basic_details_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.hlbasicdetails')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.productsandpolicy')),
            ],
        ),
        migrations.CreateModel(
            name='HlLoan_To_Value_Type_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_age', models.IntegerField()),
                ('ltv_percent_for_fresh', models.IntegerField()),
                ('ltv_percent_for_balance_transfer', models.IntegerField()),
                ('tenure_for_fresh', models.IntegerField()),
                ('tenure_for_balance_transfer', models.IntegerField()),
                ('effective_date', models.DateTimeField(blank=True, null=True)),
                ('ineffective_date', models.DateTimeField(blank=True, null=True)),
                ('basic_details_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.hlbasicdetails')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.productsandpolicy')),
            ],
        ),
        migrations.CreateModel(
            name='HlLoan_To_Value_Type_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rbi_guidelines', models.IntegerField()),
                ('amenity', models.IntegerField()),
                ('car_parking', models.BooleanField()),
                ('car_parking_amount', models.IntegerField(blank=True, null=True)),
                ('effective_date', models.DateTimeField(blank=True, null=True)),
                ('ineffective_date', models.DateTimeField(blank=True, null=True)),
                ('basic_details_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.hlbasicdetails')),
                ('loan_amount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.loanamount')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.productsandpolicy')),
            ],
        ),
        migrations.CreateModel(
            name='HlIncomeFoir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_income_foir', models.IntegerField()),
                ('max_income_foir', models.IntegerField()),
                ('income_foir_percentage', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('effective_date', models.DateTimeField(blank=True, null=True)),
                ('ineffective_date', models.DateTimeField(blank=True, null=True)),
                ('basic_details_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.hlbasicdetails')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.productsandpolicy')),
            ],
        ),
        migrations.CreateModel(
            name='HlIncome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gross_salary', models.BooleanField()),
                ('net_salary', models.BooleanField()),
                ('bonus', models.BooleanField()),
                ('min_bonus_avg_monthly', models.IntegerField()),
                ('max_bonus_avg_monthly', models.IntegerField()),
                ('bonus_avg_monthly_percentage', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('income_foir_monthly', models.BooleanField()),
                ('min_bonus_avg_quarterly', models.IntegerField()),
                ('max_bonus_avg_quarterly', models.IntegerField()),
                ('bonus_avg_quarterly_percentage', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('income_foir_quarterly', models.BooleanField()),
                ('min_bonus_avg_half_yearly', models.IntegerField()),
                ('max_bonus_avg_half_yearly', models.IntegerField()),
                ('bonus_avg_half_yearly_percentage', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('income_foir_half_yearly', models.BooleanField()),
                ('min_bonus_avg_yearly', models.IntegerField()),
                ('max_bonus_avg_yearly', models.IntegerField()),
                ('bonus_avg_yearly_percentage', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('income_foir_yearly', models.BooleanField()),
                ('rent_income', models.BooleanField()),
                ('bank_reflection', models.BooleanField()),
                ('min_rent_reflection_in_bank', models.IntegerField()),
                ('max_rent_reflection_in_bank', models.IntegerField()),
                ('rent_income_percentage', models.IntegerField()),
                ('co_applicant_no_income_only_rent_income', models.BooleanField()),
                ('co_applicant_mandatory', models.BooleanField()),
                ('future_rent', models.BooleanField()),
                ('future_rent_percentage', models.IntegerField()),
                ('income_foir_future_rent', models.IntegerField()),
                ('incentive', models.BooleanField()),
                ('min_incentive_avg_monthly', models.IntegerField()),
                ('max_incentive_avg_monthly', models.IntegerField()),
                ('incentive_avg_monthly_percentage', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('min_incentive_avg_quarterly', models.IntegerField()),
                ('max_incentive_avg_quarterly', models.IntegerField()),
                ('incentive_avg_quarterly_percentage', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('min_incentive_avg_half_yearly', models.IntegerField()),
                ('max_incentive_avg_half_yearly', models.IntegerField()),
                ('incentive_avg_half_yearly_percentage', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('min_incentive_avg_yearly', models.IntegerField()),
                ('max_incentive_avg_yearly', models.IntegerField()),
                ('incentive_avg_yearly_percentage', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('income_foir_incentive', models.BooleanField()),
                ('income_foir', models.IntegerField()),
                ('effective_date', models.DateTimeField(blank=True, null=True)),
                ('ineffective_date', models.DateTimeField(blank=True, null=True)),
                ('basic_details_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.hlbasicdetails')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.productsandpolicy')),
                ('rent_agreement_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.agreementtype')),
            ],
        ),
        migrations.AddField(
            model_name='hlbasicdetails',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.productsandpolicy'),
        ),
        migrations.AddField(
            model_name='hlbasicdetails',
            name='salary_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.salarytype'),
        ),
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('fee_id', models.AutoField(primary_key=True, serialize=False)),
                ('login_fees', models.CharField(max_length=25)),
                ('proc_fee_app', models.CharField(max_length=25)),
                ('proc_fee_type', models.CharField(max_length=25)),
                ('proc_fee_flat_loan_amtwise', models.CharField(max_length=25)),
                ('proc_fee_percent_loan_amtwise', models.CharField(max_length=25)),
                ('offers', models.CharField(max_length=25)),
                ('offline_or_online', models.CharField(max_length=7)),
                ('bank_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.bank')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.productsandpolicy')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerNationality',
            fields=[
                ('cust_nat_id', models.AutoField(primary_key=True, serialize=False)),
                ('cust_nat', models.CharField(max_length=25)),
                ('bank_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.bank')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerDesignation',
            fields=[
                ('cust_desig_id', models.AutoField(primary_key=True, serialize=False)),
                ('cust_desig', models.CharField(max_length=25)),
                ('bank_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.bank')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.productsandpolicy')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cust_id', models.AutoField(primary_key=True, serialize=False)),
                ('min_age', models.IntegerField()),
                ('total_Exp', models.IntegerField()),
                ('form16', models.CharField(max_length=3)),
                ('salary_type', models.CharField(max_length=25)),
                ('bank_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.bank')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('comp_id', models.AutoField(primary_key=True, serialize=False)),
                ('comp_type', models.CharField(max_length=25)),
                ('bank_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.bank')),
            ],
        ),
        migrations.CreateModel(
            name='Cibil',
            fields=[
                ('cibil_id', models.AutoField(primary_key=True, serialize=False)),
                ('min_amount', models.BigIntegerField()),
                ('max_amount', models.BigIntegerField()),
                ('min_cibil', models.IntegerField()),
                ('max_cibil', models.IntegerField()),
                ('min_rate', models.FloatField()),
                ('max_rate', models.FloatField()),
                ('processing_fees', models.FloatField()),
                ('effective_date', models.DateTimeField(blank=True, null=True)),
                ('ineffective_date', models.DateTimeField(blank=True, null=True)),
                ('cibil_loan_type_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='master.cibilloantype')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.productsandpolicy')),
            ],
        ),
        migrations.CreateModel(
            name='BankCodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25)),
                ('name_of_company', models.CharField(max_length=50)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.bank')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.productsandpolicy')),
            ],
        ),
        migrations.CreateModel(
            name='Age',
            fields=[
                ('age_id', models.AutoField(primary_key=True, serialize=False)),
                ('min_age', models.IntegerField()),
                ('retire_age', models.IntegerField()),
                ('max_age_consi_others', models.IntegerField()),
                ('max_age_consi_gov', models.IntegerField()),
                ('bank_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HomeLoan.bank')),
            ],
        ),
    ]
